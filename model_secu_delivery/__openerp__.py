# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Model Security Delivery',
    'category': 'Security',
    'version': '8.0.1.3.1',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'sale',
        'stock',
        'sale_line_quant',
        'sale_margin'
    ],
    'summary':"""A group for delivery users""",
    'description': """
     Accesses mostly on "sales" module \
     in sales.order, NO ADD ITEMS \
     in sales.order, NO Stock Owner, Cost Price, Margin \
     allow CONFIRM QUOTATION \
     allow DO-OUT \
    """,
    'data': [
         'security/delivery_security.xml',
         'security/base_security.xml',
         'security/ir.model.access.csv',
         'views/sale_order.xml',
    ],

    'qweb': [],
    'installable': True,
}
