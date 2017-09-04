# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class SupplierStock(models.Model):
    _inherit = "supplier.stock"

    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # two cases lead to a price change
    # 1. newly created supplier stock
    # 2. modified supplier stock
    @api.multi
    @api.depends('price_unit')
    def update_pt_price_change_date(self,record):
        #Grab all stocks of record's type
        domain = [
            ('product_id', '=', record['product_id']),
        ]
        stocks = self.search(domain)
        last_added_stock=stocks[-1]
        if last_added_stock.price_unit != record['unit_price']:
            last_added_stock.product_id.product_tmpl_id.currency_price_change_date=fields.Datetime.now()
            return True


    # case 1: record is the supplier stock to be added
    @api.model
    def create(self, vals):
        record = super(SupplierStock, self).create(vals)
        set_own_price_update_field = self.update_pt_price_change_date(record)
        if set_own_price_update_field:
            record['currency_price_change_date'] = fields.Datetime.now()
        return record


    # case 2: record is the modified  supplier stock
    @api.multi
    def write(self, vals):
        record = super(SupplierStock, self).write(vals)
        set_own_price_update_field = self.update_pt_price_change_date(record)
        if set_own_price_update_field:
            record['currency_price_change_date'] = fields.Datetime.now()
        return record
