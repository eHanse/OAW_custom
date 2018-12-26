# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Exchange rate overview',
    'category': 'Security',
    'version': '8.0.0.1',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'account',
        'model_security_adjust_oaw',
        'model_secu_eca'
    ],
    'summary':"""Provides a view of recent company currency rates for all external groups""",
    'description': """


    """,
    'data': [
         # 'security/partner_member_security.xml',
         # 'security/ir.model.access.csv',
          'views/currency_rates.xml',
         # 'views/product_template_views.xml',
         # 'views/stock_picking.xml',
    ],

    'qweb': [],
    'installable': True,
}
