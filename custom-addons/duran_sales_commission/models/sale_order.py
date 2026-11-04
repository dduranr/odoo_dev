# -*- coding: utf-8 -*-
"""
=============================================================================
ARCHIVO: sale_order.py
PROPÓSITO DIDÁCTICO:
Este archivo es una **Extensión de Lógica de Negocio de Ventas** (`sale.order` y `sale.order.line`).
Contiene los métodos computados (`@api.depends`) que calculan automáticamente
el porcentaje de comisión y el monto monetario por línea y por orden completa.
=============================================================================
"""

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    """
    Extensión de sale.order.line para incorporar el cálculo automático del porcentaje
    y monto de comisión por cada línea vendida, aplicando excepciones por producto o regla general.
    """

    _inherit = 'sale.order.line'

    commission_percentage = fields.Float(
        string='Comisión (%)',
        compute='_compute_commission_values',
        store=True,
        readonly=False,
        help='Porcentaje de comisión aplicado a esta línea de venta.'
    )
    commission_amount = fields.Monetary(
        string='Monto Comisión',
        compute='_compute_commission_values',
        store=True,
        currency_field='currency_id',
        help='Monto total de comisión calculado para esta línea.'
    )

    @api.depends('product_id', 'price_subtotal', 'order_id.state', 'order_id.company_id')
    def _compute_commission_values(self):
        """
        Calcula de forma reactiva el porcentaje y el monto de comisión por línea.
        Evalúa si existe una regla de excepción activa para el producto; de lo contrario,
        aplica el porcentaje general de la compañía. El monto se calcula condicionalmente
        solo cuando la venta se completa (estado 'sale' o 'done').
        """
        rule_model = self.env['duran.commission.rule']
        for line in self:
            percentage = 0.0
            amount = 0.0

            if line.product_id:
                company = line.order_id.company_id or self.env.company
                rule = rule_model.search([
                    ('product_id', '=', line.product_id.id),
                    ('company_id', '=', company.id),
                    ('active', '=', True)
                ], limit=1)

                if rule:
                    percentage = rule.commission_percentage
                else:
                    percentage = company.default_commission_percentage

            if line.order_id.state in ['sale', 'done']:
                subtotal = line.price_subtotal or 0.0
                amount = subtotal * (percentage / 100.0)
            else:
                amount = 0.0

            line.commission_percentage = percentage
            line.commission_amount = amount


class SaleOrder(models.Model):
    """
    Extensión de sale.order para consolidar el total de comisiones y
    la tasa de comisión ponderada de la orden completa.
    """

    _inherit = 'sale.order'

    commission_total = fields.Monetary(
        string='Total Comisión',
        compute='_compute_order_commission',
        store=True,
        currency_field='currency_id',
        help='Monto total de comisiones calculadas para esta orden de venta.'
    )
    commission_rate = fields.Float(
        string='Comisión Ponderada (%)',
        compute='_compute_order_commission',
        store=True,
        help='Porcentaje promedio ponderado de comisión en la transacción.'
    )

    @api.depends('order_line.commission_amount', 'order_line.price_subtotal', 'order_line.commission_percentage', 'amount_untaxed', 'state')
    def _compute_order_commission(self):
        """
        Calcula el monto total acumulado de comisiones de la orden y
        la tasa de comisión ponderada expresada en factor decimal (0.05 para 5%).
        """
        for order in self:
            total_comm = sum(order.order_line.mapped('commission_amount'))
            order.commission_total = total_comm
            
            total_weighted = sum(
                (line.price_subtotal or 0.0) * (line.commission_percentage or 0.0)
                for line in order.order_line
            )
            if order.amount_untaxed and order.amount_untaxed > 0:
                # Almacenado como factor decimal (ej. 0.05) para ser formateado correctamente por el widget percentage (5%)
                order.commission_rate = (total_weighted / order.amount_untaxed) / 100.0
            else:
                order.commission_rate = 0.0



