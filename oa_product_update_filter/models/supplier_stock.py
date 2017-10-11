# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class SupplierStock(models.Model):
    _inherit = "supplier.stock"

    # For filter: Overseas Currency Amount Price Change in 24h: Changed by write() or create()
    # Result in Supplier Stock: All Records of a certain product_id will be listed that were changed in the last 24h
    # Result in LPU: The product with the same product_id will be listed
    currency_price_change_date = fields.Datetime(
        string="Last Update on Currency Amount",
        store=True,
        compute="currency_price_change_date_by_update"
    )

    # For Sale HKD changes (Realized in List Price Update)
    list_price_change_date = fields.Datetime(
        string="Update listprice, HKD Retail",
        store=True,
    )

    # For a filter in Supplier Stock
    # Trigger:  supplier_stock.create()
    new_entry_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # For filter: Overseas Currency Amount Price Change in 24h
    # Case 1:. newly created supplier stock
    @api.multi
    def currency_price_change_date_by_create(self, vals):
        # Grab all stocks of record's type
        # That have the same currency
        domain = [
                ('product_id', '=', vals['product_id']),
                ('currency_id', '=', vals['currency_id']),
        ]
        last_added_stock = self.search(domain, order='create_date DESC', limit=1)
        if last_added_stock:
            if last_added_stock[0].price_unit != vals['price_unit']:
                last_added_stock[0].product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
                return True
    # For filter: Overseas Currency Amount Price Change in 24h
    # Case 2:. newly created supplier stock
    @api.multi
    @api.depends('price_unit')
    def currency_price_change_date_by_update(self):
        self.product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
        self.currency_price_change_date = fields.Datetime.now()

    @api.model
    def create(self, vals):
        # For filter: Overseas Currency Amount Price Change in 24h
        set_own_price_update_field = self.currency_price_change_date_by_create(vals)
        if set_own_price_update_field:
            vals['currency_price_change_date'] = fields.Datetime.now()
        return super(SupplierStock, self).create(vals)





