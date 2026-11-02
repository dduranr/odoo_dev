# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrderLine(models.Model):
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
        """Calcula el porcentaje y monto de comisión por línea según regla específica o por defecto."""
        rule_model = self.env['duran.commission.rule']
        for line in self:
            percentage = 0.0
            amount = 0.0

            if line.product_id:
                # Buscar regla específica para el producto en la compañía actual
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

            # Solo calcular el monto efectivo si la orden está confirmada ('sale') o en estado 'done'
            # (En borrador / cotización se puede mostrar el porcentaje estimado pero el monto se calcula o se muestra)
            # Requerimiento: "calcular automáticamente la comisión del vendedor solo cuando la venta se complete (estado confirmado/facturado)"
            # Consideramos 'sale' o 'done' (o facturado).
            if line.order_id.state in ['sale', 'done']:
                subtotal = line.price_subtotal or 0.0
                amount = subtotal * (percentage / 100.0)
            else:
                amount = 0.0

            line.commission_percentage = percentage
            line.commission_amount = amount


class SaleOrder(models.Model):
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
        help='Porcentaje promedio de comisión en la transacción.'
    )

    @api.depends('order_line.commission_amount', 'amount_untaxed', 'state')
    def _compute_order_commission(self):
        """Calcula el total de comisión y la tasa ponderada de la orden de venta."""
        for order in self:
            total_comm = sum(order.order_line.mapped('commission_amount'))
            order.commission_total = total_comm
            
            if order.amount_untaxed and order.amount_untaxed > 0:
                order.commission_rate = (total_comm / order.amount_untaxed) * 100.0
            else:
                order.commission_rate = 0.0
