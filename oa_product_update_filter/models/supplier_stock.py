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
    )

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
    def create_pt_price_change_date(self, vals):
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
    # Case 2:. updated supplier stock
    # @api.multi
    # def write_pt_price_change_date(self, vals):
    #     # Grab all stocks of record's product_id
    #     domain = [
    #             ('product_id', '=', self.product_id.id),
    #     ]
    #     stocks = self.search(domain)
    #     last_added_stock = stocks[-1]
    #     if last_added_stock.price_unit != vals['price_unit']:
    #         last_added_stock.product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
    #         return True
    @api.multi
    @api.depends('price_unit')
    def updated_currency_amout_price(self):
        self.product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
        self.currency_price_change_date = fields.Datetime.now()


    # Updates list_price_change_date
    # Here, self could contain multiple records.
    # @api.multi
    # @api.depends('product_id.product_tmpl_id.list_price_change_date')
    # def update_updated_price_change_date(self):
    #     for sup_stock in self:
    #         sup_stock.list_price_change_date = fields.Datetime.now()
    # @api.multi
    # def update_by_new_entry_date(self, vals):
    #     # Get the product_template of the supplier stock being created
    #     #tmpl = self.product_id.product_tmpl_id
    #     tmpl = vals['product_id.product_tmpl_id']
    #     # Set the date field
    #     tmpl.new_entry_date = fields.Datetime.now()
    #     # Update all date fields of it's product_id;
    #     domain = [
    #         ('product_id', '=', vals['product_id']),
    #     ]
    #     sup_stocks_of_same_product = self.env['supplier_stock'].search(domain)
    #     for rec in sup_stocks_of_same_product:
    #         rec.new_entry_date = fields.Datetime.now()


    @api.model
    def create(self, vals):
        # For Filter: Overseas Currency Amount Price Change in 24h
        #self.update_by_new_entry_date(vals)

        set_own_price_update_field = self.create_pt_price_change_date(vals)
        if set_own_price_update_field:
            vals['currency_price_change_date'] = fields.Datetime.now()
        return super(SupplierStock, self).create(vals)

    # For filter: Overseas Currency Amount Update in 24h
    # case 2: Triggering record is the modified supplier stock
    # @api.multi
    # def write(self, vals):
    #     set_own_price_update_field = self.write_pt_price_change_date(vals)
    #     if set_own_price_update_field:
    #         vals['currency_price_change_date'] = fields.Datetime.now()
    #     return super(SupplierStock, self).write(vals)




