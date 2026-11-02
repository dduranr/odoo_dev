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


