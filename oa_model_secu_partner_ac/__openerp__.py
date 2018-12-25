# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Model Security Partner AC',
    'category': 'Security',
    'version': '8.0.0.1',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'sale',
        'product_offer',
        'model_security_adjust_oaw'





    ],
    'summary':"""A group based on 'Supplier' group of model_security_adjust_oaw""",
    'description': """
     Enhances Supplier access by Product Offer views \

    """,
    'data': [
         'security/partner_ac_security.xml',
         'security/ir.model.access.csv',
          'views/sale_views.xml',
         'views/product_template_views.xml',
         # 'views/stock_picking.xml',
    ],

    'qweb': [],
    'installable': True,
}
