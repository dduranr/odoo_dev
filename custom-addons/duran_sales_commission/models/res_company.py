# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    default_commission_percentage = fields.Float(
        string='Porcentaje de Comisión por Defecto (%)',
        default=5.0,
        help='Porcentaje de comisión general aplicable a todos los productos y servicios por defecto.'
    )
