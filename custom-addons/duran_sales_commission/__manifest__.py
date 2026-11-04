# -*- coding: utf-8 -*-
"""
=============================================================================
ARCHIVO: __manifest__.py
PROPÓSITO DIDÁCTICO:
El manifiesto es el "acta de nacimiento" y descriptor principal de un módulo en Odoo.
Define metadatos esenciales como:
  - name / summary / description: Información descriptiva del módulo.
  - category / author / website: Clasificación y autoría.
  - depends: Lista de módulos prerrequisitos que deben instalarse antes (ej. 'sale_management').
  - data: Lista de archivos de seguridad, modelos y vistas XML que Odoo cargará al instalarse.
  - installable / application: Indica si es un módulo ejecutable como aplicación principal.
=============================================================================
"""

{
    'name': 'Duran Sales Commission',
    'version': '20.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Gestión avanzada de comisiones de ventas y reglas de excepción por producto para Odoo 20',
    'description': """
        Módulo personalizado de comisiones de ventas para Odoo 20:
        - Regla de comisión general por defecto (5% configurable).
        - Tabla de excepciones de comisiones por producto específico.
        - Cálculo automático de comisiones en líneas de venta y órdenes de venta confirmadas.
        - Integración en la interfaz gráfica de órdenes de venta y menú de configuración.
    """,
    'author': 'Duran / Odoo Expert',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.xml',
        'views/commission_rule_views.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}



