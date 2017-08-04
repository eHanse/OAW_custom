# -*- coding: utf-8 -*-
{
    'name': "products_sales_view",

    'summary': """
      Shows sales for each product. """,
      
    'description': """
        A view accessible through a menueitem under Sales/Products.
        Menu item links to Products/Sales. Default view shall be grouped by customer.
        Remove field "route".
        Field "subtotal" behind customer.
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
    ],

    # always loaded
    'data': [
        'views/products_sales_view.xml',
        'views/sale_view.xml',
    ],
    # only loaded in demonstration mode
    'post_init_hook': '_update_prod_tmpl_fields',
    'installable': True,
    'demo': [],
}