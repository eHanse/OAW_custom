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


    @api.multi
    def update_pt_price_change(self,vals):
        # Situation: Many2one to Many2one)
        # Relations of the involved models: stock.quant to product.product (Many2One)
        # and product.product to product.template (Many2One).
        # Meaning: If stock.quant A and stock.quant B belong to product.product Z,
        # both stock.quant belong automatically to product.template R .

        # Get all quants
        # that are of the same product (template) like record
        # that are VCI quants (owner_id = 1 is company)
        domain = [
            ('product_id', '=', vals['product_id']),
            ('owner_id', '!=', 1),
        ]
        # This tuple should limit qnts to have only VCI. But it is not working.
        # ('owner_id', '!=', 1),
        qnts = self.env['stock.quant'].search(domain, order='create_date DESC')
        if qnts:
            last_quant = qnts[0]
        # Get purchase_price_unit of quant being created by accessing it's last stock_move (assuming it is a DO-IN)
        # Are quants not only created by DO-INs ?
        domain = [
            ('product_id', '=', vals['product_id']),
            ('quant_owner_id', '!=', 1),
        ]
        its_stock_move = self.env['stock.move'].search(domain, order='create_date DESC')
        if its_stock_move:
          current_purchas_price = its_stock_move[0].purchase_price_unit

        if last_quant.purchase_price_unit != current_purchas_price:
            # In case the price changed, we set its product_template field related to price changes
            last_quant.product_id.product_tmpl_id.currency_price_change_date=fields.Datetime.now()

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


    # Price change for VCI only possible by DO-INs, which will call - presumable - call the create function
    # Record is the stock being added
    @api.model
    def create(self,vals):
        self.update_pt_price_change(vals)
        self.update_new_entry(vals)
        return super(StockQuant, self).create(vals)
