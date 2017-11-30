# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

from addons.OAW_custom.oa_product_update_filter.models import product_product


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # updated_c24_date = fields.Datetime(
    #     string="Updated C24 Date",
    #     store=True,
    #     compute="update_c24_date"
    # )

    # For a filter in Product and Product Offer views.
    # Trigger: stock.quant (stock_move.purchase_price_unit), supplier_stock.price_unit
    currency_price_change_date = fields.Datetime(
        string="Currency Amount Price Change Date",
        store=True,
    )

    # For a filter
    # Effective in Product and Product Offer
    # Trigger: product_template.list_price "Retail HKD"
    list_price_change_date = fields.Datetime(
        string="Retail HKD Change Date",
        store=True,
        compute="update_list_price_change_date"
    )

    # For a filter in Product and Product Offer: New Stock Entry 24
    # Trigger: stock_quant.create(), supplier_stock.create()
    new_entry_date = fields.Datetime(
        string="New Entry",
        store=True,
    )

    # For a filter in Product and Product Offer
    # Trigger: product_template.write(),
    # Trigger: product_product.price_up_date
    price_up_date = fields.Datetime(
        string="Sale HKD Price Up Date",
        store=True,
    )

    # For a filter in Product and Product Offer
    # Trigger: product_template.write(),
    # Trigger: product_product.price_up_date
    price_down_date = fields.Datetime(
        string="Sale HKD Price Down Date",
        store=True,
    )

    # Field that listens to changes associated to chrono24 filter
    updated_chrono24 = fields.Datetime(
        store=True,
        default=False,
        string="Updated Chrono24 Date",
    )

    chrono24_price = fields.Float(
        string='Chrono24 Price',
        store=True,
    )

    # For Filter Sale HKD up down
    @api.multi
    def write(self, vals):
        for pt in self:
            if 'net_price' in vals or 'stock_cost' in vals or 'chrono24_price' in vals or 'qty_reserved' in vals or 'qty_local_stock' in vals or 'qty_overseas' in vals:
                # Method for chrono24
                vals['updated_chrono24'] = self.updated_chrono24_date(pt,vals)
                # get the current price
                if 'net_price' in vals:
                    curr_net_price = pt.net_price
                    if curr_net_price < vals['net_price']:
                        vals['price_up_date'] = fields.Datetime.now()
                    elif curr_net_price > vals['net_price']:
                        vals['price_down_date'] = fields.Datetime.now()
        return super(ProductTemplate, self).write(vals)


    @api.multi
    @api.depends('list_price')
    def update_list_price_change_date(self):
        for pt in self:
            pt.list_price_change_date = fields.Datetime.now()



    @api.multi
    def updated_chrono24_date(self,pt,vals):
        if 'qty_local_stock' in vals and 'qty_reserved' in vals:
            stock_situation = vals['qty_local_stock'] - vals['qty_reserved']
        elif 'qty_local_stock' in vals:
            stock_situation = vals['qty_local_stock'] - pt.qty_reserved
        elif 'qty_reserved' in vals:
            stock_situation = pt.qty_local_stock - vals['qty_reserved']
        if stock_situation and stock_situation >= 0:
            return fields.Datetime.now()
        if 'stock_cost' in vals:
            if pt.stock_cost != vals['stock_cost']:
                return fields.Datetime.now()
        if 'chrono24_price' in vals:
            if pt.chrono24_price != vals['chrono24_price']:
                return fields.Datetime.now()
        return False

    @api.multi
    def updated_chrono24_date_button(self):
        for pt in self:
            pt.updated_chrono24 = fields.Datetime.now()
