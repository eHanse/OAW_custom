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
    def update_pt_price_rise(self,record):
        # Relations of involved models: quant to product.product (Many2One) and product.product to product.template (Many2One)
        # Meaning: If quant A and quant B belongs product.product Z, both belong automatically to product.template R (Many2one to Many2one)
        # Get all quants
        # that are of the same product (template) like record
        # that are VCI quants (owner_id=1 is company)
        domain = [
            ('product_id', '=', record['product_id']),
            ('owner_id', '!=', 1),
        ]
        quants = self.search(domain)
        length = len(quants)
        # Assuming that in Python lists are extended at their rear, last element in list is last added.
        # Module where pruchase_price_unit is defined might need to be added to __openerp__
        last_quant = quants[length-1]
        if last_quant.purchase_price_unit != record['purchase_price_unit']:
            # In case the price changed, we set its product_template field related to price changes
            last_quant.product_id.product_tmpl_id.price_change_date=fields.Datetime.now()

    @api.model
    def create(self,vals):
        record = super (StockQuant, self).create(vals)
        self.update_pt_price_rise(record)
        return record