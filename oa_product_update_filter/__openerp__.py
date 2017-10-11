# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Update Filter',
    'version': '0.1',
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
        1. Adds c24-Filters; 2. Currency
    """,
    'data': [
            'views/product_template_views.xml',
            'views/supplier_stock_views.xml',
    ],
    'installable': True,
}
