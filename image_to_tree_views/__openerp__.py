# -*- coding: utf-8 -*-
{
    'name': "Images to tree views",

    'summary': """
     Makes images visible in Quants and On Purchase Order Line. """,

    'description': """
         Adds image_small from product_template to tree views Quants and OPOL
    """,

    'author': "OA Watches",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ["base","purchase","sale_line_quant","purchase_view_adjust_oaw","account","stock_view_adjust_oaw"],

    # always loaded
    'data': ["views/purchase_views.xml",
             "views/quants_view.xml"],
    'installable': True,    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}