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

from openerp import models, fields, api



class StockQuant(models.Model):
    _inherit = 'stock.quant'

    # For New Entry Filter
    @api.multi
    def update_new_entry(self, vals):
        # Get the product_template of the quant being created
        #tmpl = self.product_id.product_tmpl_id
        domain = [
            ('id', '=', vals['product_id']),
        ]
        tmpl = self.env['product.product'].search(domain)[0].product_tmpl_id
        # Set the date field
        tmpl.new_entry_date = fields.Datetime.now()


    # Price change for VCI only possible by DO-INs, which will  - presumable - call the create function
    # Record is the stock being added
    @api.model
    def create(self,vals):
        #self.new_vci_pt_price_change(vals)
        self.update_new_entry(vals)
        return super(StockQuant, self).create(vals)

