# -*- coding: utf-8 -*-
# Copyright 2015-2018 Quartile Limted
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Listprice List View (Short)',
    'version': '8.0.0.1',
    'author': 'joa, eHanse, Quartile',
    'website': 'https://www.quartile.co',
    'category': 'Product',
    'depends': [
        "sale",
        "stock",
        "product_offer",
        "supplier_stock_hk_location",
        "product_listprice_list_view",
        "oa_product_update_filter"
    ],
    'description': """
* Adds an abbreviated view based on PLU.
    """,
    'data': [
        'views/product_product_views.xml',
    ],
    'installable': True,
}
