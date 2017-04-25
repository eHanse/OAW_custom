# -*- coding: utf-8 -*-
{
    'name': "oa_adj_list_price_update",

    'summary': """
      Modifies List Price Update tree view. """,
      
    'description': """
        Changes the order of fields shown in List Price Update;
        Adds seller_delay to List Price Update;
        Adds 2 new fields to models product.template;
        1.) boolean that shows which products can be advertised for;
        2.) Computed field that calculates the discount from List Price to HK Net price
    """,

    'author': "OA Watches",    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ["base","product",],

    # always loaded
    'data': ["list_price_update_update.xml"],
    'installable': True,    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}