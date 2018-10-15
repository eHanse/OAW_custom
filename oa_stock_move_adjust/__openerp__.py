# -*- coding: utf-8 -*-
{
    'name': "Get Source Document",

    'summary': """
      Displays Stock Pickings Oirigin field in Stock Move. """,

    'description': """

    """,

    'author': "OA Watches",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ["base",
                "stock",
                "stock_view_adjust_oaw",
                ],
    # always loaded
    'data': [
#              "views/purchase_views.xml",
             "views/stock_move_ext.xml",
             ],
    'installable': True,    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}