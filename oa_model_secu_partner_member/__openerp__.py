# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Model Security Partner Member',
    'category': 'Security',
    'version': '8.0.0.1',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'sale',
        'product_offer',
        'model_security_adjust_oaw',
        'oa_model_secu_partner_ac',






    ],
    'summary':"""A group based on 'Supplier' group of model_security_adjust_oaw and extends Parnter AC group""",
    'description': """
     Extension to Supplier and Partner AC. \

    """,
    'data': [
         'security/partner_member_security.xml',
         'security/ir.model.access.csv',
          'views/stock_offer.xml',
         # 'views/product_template_views.xml',
         # 'views/stock_picking.xml',
    ],

    'qweb': [],
    'installable': True,
}
