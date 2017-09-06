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
        # Relations of the involved models: stock.quant to product.product (Many2One)
        # and product.product to product.template (Many2One).
        # Meaning: If stock.quant A and stock.quant B belong product.product Z,
        # both stock.quant belong automatically to product.template R (Many2one to Many2one).
        # Get all quants
        # that are of the same product (template) like record
        # that are VCI quants (owner_id = 1 is company)
        domain = [
            ('product_id', '=', vals['product_id']),
        ]
        # ('owner_id', '!=', 1),
        qnts = self.env['stock.quant'].search(domain)
        # Get purchase_price_unit of quant being created by accessing it's last stock_move (assuming it is a DO-IN)
        # Are quants not only created by DO-INs ?
        domain = [
            ('product_id', '=', vals['product_id']),
        ]
        current_purchase_price = self.env['stock.move'].search(domain)[0].purchase_price_unit
        last_quant = qnts[0]
        if last_quant.purchase_price_unit != current_purchase_price:
            # In case the price changed, we set its product_template field related to price changes
            last_quant.product_id.product_tmpl_id.currency_price_change_date=fields.Datetime.now()

    # Price change for VCI only possible by DO-INs, which will call - presumable - call the create function
    # Record is the stock being added
    @api.model
    def create(self,vals):
        self.update_pt_price_change(vals)
        return super(StockQuant, self).create(vals)
