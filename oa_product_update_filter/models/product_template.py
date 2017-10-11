# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    updated_c24_date = fields.Datetime(
        string="Updated C24 Date",
        store=True,
        compute="update_c24_date"
    )

    #For a filter in Product and Product Offer views.
    # Trigger: stock.quant (stock_move.purchase_price_unit), supplier_stock.price_unit
    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    #For a filter in Product and Product Offer
    # Trigger: product_template.list_price
    list_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # For a filter in Product and Product Offer
    # Trigger: stock_quant.create(), supplier_stock.create()
    new_entry_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # For a filter in Product and Product Offer
    # Trigger: product_template.write(),
    # Trigger: product_product.price_up_date
    price_up_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # For a filter in Product and Product Offer
    # Trigger: product_template.write(),
    # Trigger: product_product.price_up_date
    price_down_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # def price_check(self,vals):
    #     # get the current price
    #     curr_net_price = self.net_price
    #     if curr_net_price < vals['net_price']:
    #         self.price_up_date = fields.Datetime.now()
    #     elif curr_net_price > vals['net_price']:
    #         self.price_down_date = fields.Datetime.now()
    #
    @api.multi
    @api.depends('chrono')
    def update_c24_date(self):
        for p in self:
            self.updated_c24_date = fields.Datetime.now()

    @api.multi
    @api.depends('list_price')
    def update_updated_date(self):
        for pt in self:
            pt.list_price_change_date = fields.Datetime.now()

    # Whats that for ??????????
    # @api.multi
    # def write(self, vals):
    #     #self.price_check(vals)
    #     return super(ProductTemplate, self).write(vals)

