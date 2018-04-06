# -*- coding: utf-8 -*-
{
    'name': "oa_chrono24_view",

    'summary': """
      Creates a distinct view for chono24. """,
      
    'description': """
        View accessible through Sales/ and will replace ListPriceUPdate view
        for standard Sales user. Bases on Listprice Update.
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
                "sale_stock",
                "product_offer",
                "product_listprice_list_view",
                "oa_product_update_filter",
    ],

    # always loaded
    'data': [
        'views/chrono24_views.xml',
        #'views/sale_view.xml',
    ],
    # only loaded in demonstration mode
    #'post_init_hook': '_update_prod_tmpl_fields',
    'installable': True,
    'demo': [],
}