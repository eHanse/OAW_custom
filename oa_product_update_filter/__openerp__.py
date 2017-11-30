# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Update Filter',
    'version': '0.8',
    'author': 'oa-trade',
    'website': 'oa-trade.com',
    'category': 'Product',
     'depends': [
        "sale_line_quant",
        "product",
        "product_offer",
        "product_listprice_list_view",
        "supplier_stock",
    ],

    'description': """
        1. Adds c24-Filters; 2. Adds Change Date Filters for Supplier Stock and Product/LPU views
        2. new special chrono24 mechanics
    """,
    'data': [
            'views/product_template_views.xml',
            'views/supplier_stock_views.xml',
    ],
    'installable': True,
}
