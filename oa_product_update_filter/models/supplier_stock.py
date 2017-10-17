# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class SupplierStock(models.Model):
    _inherit = "supplier.stock"

    # For filter: Overseas Currency Purchase Price Unit Change in 24h: Changed by updating existing entry or creating new entry
    # Result in Supplier Stock: All Records of a certain product_id will be listed that were changed/created in the last 24h
    # Result in LPU: The product with the same product_id will be listed
    currency_price_change_date = fields.Datetime(
        string="Last Update on Currency Amount",
        store=True,
        #compute="currency_price_change_date_by_update"
    )

    # For Sale HKD changes (Realized in List Price Update)
    list_price_change_date = fields.Datetime(
        string="Update listprice, HKD Retail",
        store=True,
    )

    # For a filter in Supplier Stock
    # Trigger:  supplier_stock.create()
    new_entry_date = fields.Datetime(
        string="New Supplier Stock",
        store=True,
    )

    # For Purchase Price Unit filter: Modify existing entry
    @api.multi
    def write(self, vals):
        if 'price_unit' in vals:
            for stock in self:
                vals['currency_price_change_date'] = fields.Datetime.now()
                stock.product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
        res = super(SupplierStock, self).write(vals)
        return res


   # For Purchase Price Unit filter: create Entry of same product with different price
    #For New Entry Filter: Create New Entry with Product; new entry but same price
    @api.model
    def create(self, vals):
        if 'product_id' in vals and 'currency_id' in vals:
            # Check for existing supplier stocks
            # And get the last one
            domain = [
                ('product_id', '=', vals['product_id']),
                ('currency_id', '=', vals['currency_id']),
            ]
            last_added_stock = self.search(domain, order='create_date DESC')
            # For New Entry filter : New stock model
            if not last_added_stock:
                vals['new_entry_date'] = fields.Datetime.now()
                secondDomain = [
                    ('id', '=', vals['product_id']),
                ]
                product_ref = self.env['product.product'].search(secondDomain, order='create_date DESC', limit=1)
                if product_ref:
                    product_ref[0].product_tmpl_id.new_entry_date = fields.Datetime.now()
            # For Purchase Price Unit filter
            else:
                # Purchase price unit change
                if last_added_stock[0].price_unit != vals['price_unit']:
                    vals['currency_price_change_date'] = fields.Datetime.now()
                    last_added_stock[0].product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
                # For New Entry filter : New Stock with same price but maybe different supplier
                else:
                    vals['new_entry_date'] = fields.Datetime.now()
                    last_added_stock[0].product_id.product_tmpl_id.new_entry_date = fields.Datetime.now()
        res = super(SupplierStock, self).create(vals)
        return res

