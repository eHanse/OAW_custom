# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Model Chrono24 and Photo Edit',
    'category': 'Security',
    'version': '8.0.0.1',
    'author': 'OA Trade Ltd.',
    'website': '',
    'depends': [
        'product',
        "oa_product_update_filter",
    ],
    'summary':"""A group for editing Chrono24 Information and Photos""",
    'description': """
     Write access on product.template (Photo) \
     Write access on product.product (Chrono24)\
    """,
    'data': [
         'security/chr24_photo_edit_security.xml',
         'views/warehouse_views.xml',
         'security/ir.model.access.csv',
    ],

    'qweb': [],
    'installable': True,
}
