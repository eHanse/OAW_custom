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

    #For VCI Currency Amount Price Change Filter
    @api.multi
    def new_vci_pt_price_change(self,vals):
        # Get all quants
        # that are of the same product (template) like record
        # that are VCI quants (owner_id != 1 is company)
        # disregarding the location
        domain = [
            ('product_id', '=', vals['product_id']),
            ('owner_id', '!=', 1),
            ('location_id', '=', 12),
        ]
        qnts = self.env['stock.quant'].search(domain, order='create_date DESC')

        # # Assuming that vals history_ids has only one tuple of 2 values on creation!
        # history_ids_tuple = vals['history_ids'][0]
        # stock_move_id = history_ids_tuple[1]
        # domain = [
        #     ('id', '=', stock_move_id),
        # ]
        # Get all stock moves with
        # the product_id of the stock.quant record to be updated
        domain = [
            ('product_id', '=', vals['product_id']),
            ('quant_owner_id', '!=', 1),
            ('location_dest_id', '=', 12),
            ('state', '=', 'assigned'),
        ]
        stock_moves = self.env['stock.move'].search(domain, order='create_date DESC')
        if qnts:
            if stock_moves:
                if qnts[0].purchase_price_unit != stock_moves[0].purchase_price_unit:
                    # In case the price changed, we set the corresponding date field
                    qnts[0].product_id.product_tmpl_id.currency_price_change_date=fields.Datetime.now()


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
        self.new_vci_pt_price_change(vals)
        self.update_new_entry(vals)
        return super(StockQuant, self).create(vals)

