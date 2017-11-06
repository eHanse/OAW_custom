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
    'name': 'Adjustments on Quotation Report',
    'version': '0.7',
    'author': 'eHanse IT and Consulting UG',
    'website': 'https://ehanse.de',
    'category': 'Accounting',
    'depends': ["account",],
    'description': """
* Makes adjustments on quotation print output to show 1.case number 2.table 3.replace comments
    """,
    'depends': [
        "sale",
    ],
    'data': [
        'views/report_saleorder.xml',
    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
