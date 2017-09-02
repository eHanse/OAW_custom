# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) eHanse UG https://ehanse.de.
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
    'name': 'Adds new report and print option to status bar',
    'version': '0.8',
    'author': 'OA Trading',
    'website': 'oa-trade.com',
    'category': 'Report',
    'depends': ["sale",
                "account",
                "report",
    ],
    'description': """
        * New report type for quotation. New print button in quotation/sales order workflow
    """,
    'data': [
        'report/report_sale_order_sino.xml',
        'views/sale_view.xml',
    ],
    "qweb":[

    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
