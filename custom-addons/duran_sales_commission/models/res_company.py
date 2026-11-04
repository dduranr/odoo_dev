# -*- coding: utf-8 -*-
"""
=============================================================================
ARCHIVO: res_company.py
PROPÓSITO DIDÁCTICO:
Este archivo es una **Extensión de Modelo Base** (`res.company`).
Permite añadir campos a la tabla de compañías de Odoo. Aquí agregamos el
porcentaje de comisión general por defecto (5%) a nivel empresarial.
=============================================================================
"""

from odoo import models, fields


class ResCompany(models.Model):
    """
    Extensión del modelo res.company para incorporar el parámetro de
    porcentaje de comisión general aplicable por defecto a todos los productos.
    """

    _inherit = 'res.company'

    default_commission_percentage = fields.Float(
        string='Porcentaje de Comisión por Defecto (%)',
        default=5.0,
        help='Porcentaje de comisión general aplicable a todos los productos y servicios por defecto.'
    )


