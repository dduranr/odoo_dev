# -*- coding: utf-8 -*-
"""
=============================================================================
ARCHIVO: res_config_settings.py
PROPÓSITO DIDÁCTICO:
Este archivo es una **Extensión de Modelo Transient** (`res.config.settings`).
Los modelos Transient en Odoo son temporales y se usan para la interfaz de Ajustes.
Conecta los ajustes visuales con el campo guardado en la compañía (`res.company`).
=============================================================================
"""

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    """
    Extensión de res.config.settings para permitir al administrador configurar
    el porcentaje de comisión general por defecto desde la interfaz de Ajustes de Ventas.
    """

    _inherit = 'res.config.settings'

    sale_commission_percentage = fields.Float(
        string='Porcentaje de Comisión General (%)',
        related='company_id.default_commission_percentage',
        readonly=False,
        help='Porcentaje de comisión general aplicable a todas las ventas de forma predeterminada.'
    )





