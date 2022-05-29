# -*- coding: utf-8 -*-

{
    'name': "Generate Products Barcode",
    'summary':'This module using for odoo product barcode number generate. You can alos add prefix of your company.',
    'description': """
        product barcode number generate,
    """,
    'version': '13.0.0.1',
    'category': 'Inventory',
    'author': 'support@ingenioso.co',
    'price': '0',
    'sequence': 0,
    'depends': [ 'base', 'stock' ],
    'demo': [],
    'data': [
        'wizards/product_product_barcode.xml',
        'wizards/product_template_barcode.xml',
        'views/setting.xml',
    ],
    'images': ['static/description/generate_product_barcode_banner.png'],
    'license': 'AGPL-3',
    "currency": 'COP',
    'installable': True,
    'application': True,
    'auto_install': False,
}
