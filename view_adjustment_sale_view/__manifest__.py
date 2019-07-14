# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Rooms For (Hong Kong) Limited T/A OSCG (<http://www.openerp-asia.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'View adjustments',
    'version': '0.6',
    'author': 'eHanse',
    'website': 'https://www.ehanse.de',
    'category': 'Not a Partner yet',
    'depends': ["base",
                "sale",
                "account_voucher",
                "sale_line_quant",
                "sale_line_quant_extended",
                "stock",
                "oa_order_line_views"
                ],
    'description': """
* moves and creates, makes tabs invisible, minor adjustments on Customer/Supplier Payments
    """,
    'data': [
        'views/sale_view.xml',
        'views/sale_stock_view.xml',
    ],
    'installable': True,
}

