# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class SupplierStock(models.Model):
    _inherit = "supplier.stock"

    #For a filter in Supplier Stock list view
    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
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

    # two cases lead to a price change
    # 1. newly created supplier stock
    # 2. modified supplier stock
    @api.multi
    def create_pt_price_change_date(self, vals):
        #Grab all stocks of record's type
        domain = [
                ('product_id', '=', vals['product_id']),
        ]
        stocks = self.search(domain)
        last_added_stock = stocks[0]
        if last_added_stock.price_unit != vals['price_unit']:
            last_added_stock.product_id.product_tmpl_id.currency_price_change_date=fields.Datetime.now()
            return True

    @api.multi
    def write_pt_price_change_date(self, vals):
        # Grab all stocks of record's product_id
        domain = [
                ('product_id', '=', self.product_id.id),
        ]
        stocks = self.env['supplier.stock'].search(domain)
        last_added_stock = stocks[-1]
        if last_added_stock.price_unit != vals['price_unit']:
            last_added_stock.product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
            return True

    # Updates list_price_change_date
    # Here, self could contain multiple records.
    @api.multi
    @api.depends('product_id.product_tmpl_id.list_price_change_date')
    def update_updated_price_change_date(self):
        for sup_stock in self:
            sup_stock.list_price_change_date = fields.Datetime.now()

    @api.multi
    def update_new_entry_date(self, vals):
        # Get the product_template of the quant being created
        #tmpl = self.product_id.product_tmpl_id
        tmpl = vals['product_id.product_tmpl_id']
        # Set the date field
        tmpl.new_entry_date = fields.Datetime.now()
        # Update all date fields of it's product_id;
        domain = [
            ('product_id', '=', vals['product_id']),
        ]
        sup_stocks_of_same_product = self.env['supplier_stock'].search(domain)
        for rec in sup_stocks_of_same_product:
            rec.new_entry_date = fields.Datetime.now()


    # case 1: record is the supplier stock to be added
    @api.model
    def create(self, vals):
        self.update_new_entry_date(vals)
        set_own_price_update_field = self.create_pt_price_change_date(vals) #
        if set_own_price_update_field:
            vals['currency_price_change_date'] = fields.Datetime.now()
        return super(SupplierStock, self).create(vals)


    # case 2: record is the modified supplier stock
    @api.multi
    def write(self, vals):
        set_own_price_update_field = self.write_pt_price_change_date(vals)
        if set_own_price_update_field:
            vals['currency_price_change_date'] = fields.Datetime.now()
        return super(SupplierStock, self).write(vals)



