# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Adjust Account Move',
    'category': 'Adjustment',
    'version': '8.0.0.8',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'account',
    ],
    'summary':"""Visual Adjustments""",
    'description': """
        Makes account.view_move_tree editable
    """,
    'data': [
          'views/account_move.xml',
    ],

    'qweb': [],
    'installable': True,
}
