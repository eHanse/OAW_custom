# -*- coding: utf-8 -*-
{
    'name': "Adjustment of description field",

    'summary': """
          Adds adjusted description field to various views
    """,

    'description': """
      product_id field replaced in various tree views \n
        by default_code and new description field\n
    """,

    'author': "OA Trade",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ["base",
                "purchase",
                "sale_line_quant",
                "purchase_view_adjust_oaw",
                'account',
                'stock_transfer_lot_filter',
                'stock_view_adjust_oaw',

                ],

    # always loaded
    'data': ["views/purchase_views.xml",
             "views/account_invoice_views.xml",
             "views/stock_move_views.xml",
             "views/stock_quant.xml",
             "views/stock_transfer_details.xml",
             ],
    'installable': True,    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}