# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DuranCommissionRule(models.Model):
    """Modelo para la configuración de reglas de comisión excepcionales por producto."""

    _name = 'duran.commission.rule'
    _description = 'Regla de Comisión por Producto'
    _rec_name = 'product_id'

    product_id = fields.Many2one(
        'product.product',
        string='Producto',
        required=True,
        ondelete='cascade',
        help='Producto específico al que se aplica esta regla de comisión excepcional.'
    )
    commission_percentage = fields.Float(
        string='Porcentaje de Comisión (%)',
        required=True,
        default=10.0,
        help='Porcentaje de comisión personalizado para incentivar la venta de este producto.'
    )
    company_id = fields.Many2one(
        'res.company',
        string='Compañía',
        required=True,
        default=lambda self: self.env.company,
        help='Compañía a la que pertenece esta regla de excepción.'
    )
    active = fields.Boolean(
        string='Activo',
        default=True,
        help='Si está desactivo, esta regla no se aplicará en el cálculo de comisiones.'
    )
    note = fields.Text(
        string='Notas / Justificación',
        help='Motivo o detalles de la regla excepcional de comisión.'
    )

    @api.constrains('commission_percentage')
    def _check_commission_percentage(self):
        """Valida que el porcentaje de comisión esté entre 0 y 100."""
        for record in self:
            if record.commission_percentage < 0.0 or record.commission_percentage > 100.0:
                raise ValidationError('El porcentaje de comisión debe estar comprendido entre 0% y 100%.')

