# -*- coding: utf-8 -*-

{
    'name': "Generate Products Barcode",
    'summary':'This module using for odoo product barcode number generate. You can alos add prefix of your company.',
    'description': """
        product barcode number generate,
    """,
    'version': '13.0.0.1',
    'category': 'Inventory',
    'author': '',
    'price': '0',
    'sequence': 0,
    'depends': [ 'base', 'stock' ],
    'demo': [],
    'data': [
        'wizards/product_product_barcode.xml',
        'wizards/product_template_barcode.xml',
        'views/setting.xml',
    ],
    'qweb': [],
    "currency": 'USD',
    'installable': True,
    'application': True,
    'images': ['static/description/generate_product_barcode_banner.png'],
    'support': '',
    "license": "",
}
