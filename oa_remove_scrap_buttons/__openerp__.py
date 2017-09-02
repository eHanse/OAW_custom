# -*- coding: utf-8 -*-
{
    'name': "remove_scrap_button",

    'summary': """
      Hides scrap buttons. """,
      
    'description': """
        Hides scrap buttons of stock_view.xml.
    """,

    'author': "OA Trade",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base",
                "product",
                "decimal_precision",
                "sale",
                "stock",
    ],

    # always loaded
    'data': [
        'views/stock_view.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'demo': [],
}