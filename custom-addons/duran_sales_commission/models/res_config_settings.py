# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_commission_percentage = fields.Float(
        string='Porcentaje de Comisión por Defecto (%)',
        related='company_id.default_commission_percentage',
        readonly=False,
        help='Porcentaje de comisión general aplicable a todas las ventas de forma predeterminada.'
    )
