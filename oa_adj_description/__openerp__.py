# -*- coding: utf-8 -*-
{
    'name': "Adjustment of description field",

    'summary': """
          Adds adjusted description field to various views
    """,

    'description': """
      Field adjusted
        in RFQ \n
        in 'Supplier Invoice', \n
        in 'Stock Moves' behind Product name field, \n
        in 'Partner Stock Offer' behind Product name field, \n
        in 'Invoice Lines' behind Product name field, \n
        in 'Quants' behind Product name field, \n
        in 'Receipts' and 'Internal Transfer' form views, behind Product name \n
        in 'Transfer' pop-up \n
        in 'Profit & Loss Report' behind Reference field \n
    """,

    'author': "OA Trade",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.',

    # any module necessary for this one to work correctly
    'depends': ["base",
                "purchase",
                "sale_line_quant",
                "purchase_view_adjust_oaw",
                'account'],

    # always loaded
    'data': ["views/purchase_views.xml",
             "views/account_invoice_views.xml",
             "views/stock_move_views.xml",
             ],
    'installable': True,    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}