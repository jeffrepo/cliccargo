# -*- coding: utf-8 -*-


{
    'name': 'Clic Cargo',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Modulo Clic Cargo',
    'description': """

""",
    'depends': ['sale','purchase','account'],
    'data': [
        'views/report.xml',
        'views/sale_views.xml',
        'views/reporte_factura.xml',
        'views/purchase_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
