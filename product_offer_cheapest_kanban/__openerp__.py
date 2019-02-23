# -*- coding: utf-8 -*-
# Copyright 2017-2019 Quartile Limited
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Offer Cheapest Kanban',
    'version': '8.0.2.1.0',
    'author': 'Quartile Limited, eHanse',
    'website': 'https://www.quartile.co',
    'category': 'Product',
    'depends': [
        'product',
        'product_offer',
        'product_listprice_list_view'
    ],
    'description': """
        Adds cheapest Overseas Retail in Currency into Product Offer views if overseas quantity >0
    """,
    'data': [
        'product_template_views.xml',
    ],
    'installable': True,
}
