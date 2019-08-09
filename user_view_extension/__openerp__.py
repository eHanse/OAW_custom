# -*- coding: utf-8 -*-
# Copyright 2015-2018 Quartile Limted
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'External User List View',
    'version': '8.0.0.1',
    'author': 'eHanse',
    'website': 'https://ehanse.de',
    'category': '',
    'depends': [
        'auth_crypt',
       
    ],
    'description': """
* Adds a External User tree view next to User default view
    """,
    'data': [
        'views/view_user_tree.xml',
    ],
    'installable': True,
}
