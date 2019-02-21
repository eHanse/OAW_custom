# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Model Security End Customer Availability',
    'category': 'Security',
    'version': '8.0.0.1',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'sale',
        'product_offer',
        'product'





    ],
    'summary':"""A group for the End Customer Availablity user""",
    'description': """
     Accesses mostly on "sales" module \

    """,
    'data': [
         'security/eca_security.xml',
         'security/base_security.xml',
         'security/ir.model.access.csv',
          'views/sale_views.xml',
         'views/product_template_views.xml',
         # 'views/stock_picking.xml',
    ],

    'qweb': [],
    'installable': True,
}
