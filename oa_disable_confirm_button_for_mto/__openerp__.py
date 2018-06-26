# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'oa_disable_confirm_button_for_mto',
    'version': '0.1',
    'author': 'oa-trade',
    'website': 'oa-trade.com',
    'category': 'Sale',
    'depends': [
        "sale",
        "model_security_adjust_oaw"
    ],
    'description': """
        Makes confirm button invisable for is_mto is True
    """,
    'data': [
            'views/sale_view.xml',
    ],
    'installable': True,
}
