# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = "product.template"

    chrono = fields.Boolean(
        default=False
    )
    # button for new simplified chrono mechanics
    chrono24_updated = fields.Boolean(
        default=False
    )
    chronoNote = fields.Char(
        string="Note Chrono24"
    )

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
    updated_date_chrono24 = fields.Datetime(
        store=True,
        default=False,
        string="Updated Chrono24 Date",
    )

    chrono24_price = fields.Float(
        string='Chrono24 Price',
        digits=dp.get_precision('Product Price'),
        store=True,
    )

    # For Partner Stock filter
    qty_up = fields.Boolean(
        string='Quantity increased',
        store=True

    )
    qty_down = fields.Boolean(
        string='Quantity decreased',
        store=True
    )
    costprice_up = fields.Boolean(
        string='Costprice increased',
        readonly=True,
        store=True

    )
    costprice_down = fields.Boolean(
        string='Costprice decreased',
        readonly=True,
        store=True
    )
    note_updated = fields.Boolean(
        string='Partner Note updated',
        store=True

    )

    partner_offer_checked = fields.Boolean(
        string='Offer Checked',
        default=False,
        store=True
    )

    # For Filter Sale HKD up down
    @api.multi
    def write(self, vals):
        for pt in self:
            # Chrono24 Mechanic: Only if the product template is already activated
            if pt.chrono:
                if 'list_price' in vals or 'net_price' in vals or 'stock_cost' in vals or \
                    'chrono24_price' in vals or 'qty_reserved' in vals or 'qty_local_stock' in vals  \
                     or 'qty_overseas' in vals:
                    if self.updated_chrono24_date(pt,vals):
                        pt.updated_date_chrono24 = fields.Datetime.now()
                        # Field defined in different module, though
                        pt.chrono24_updated = True
            # Chrono24 Mechanic: Or if product template is getting activated
            if 'chrono' in vals:
                # In both case: if turned on or turned off, the chrono24 offer has to be taken care of
                if vals['chrono']:
                    pt.updated_date_chrono24 = fields.Datetime.now()
                    pt.chrono24_updated = True
                else:
                    pt.updated_date_chrono24 = fields.Datetime.now()
                    pt.chrono24_updated = True
            # Price UP and DOWN filter: get the current price
            if 'net_price' in vals:
                curr_net_price = pt.net_price
                if curr_net_price < vals['net_price']:
                    vals['price_up_date'] = fields.Datetime.now()
                elif curr_net_price > vals['net_price']:
                    vals['price_down_date'] = fields.Datetime.now()
            # For partner update
            if 'qty_local_stock' in vals and 'qty_reserved' in vals:
                if vals['qty_local_stock'] - vals['qty_reserved'] == 0:
                    self.partner_offer_checked = False
            elif 'qty_local_stock' in vals:
                if vals['qty_local_stock'] - pt.qty_reserved == 0:
                    self.partner_offer_checked = False
        return super(ProductTemplate, self).write(vals)


    @api.multi
    @api.depends('list_price')
    def update_list_price_change_date(self):
        for pt in self:
            pt.list_price_change_date = fields.Datetime.now()



    @api.multi
    def updated_chrono24_date(self,pt,vals):
        if 'qty_local_stock' in vals and 'qty_reserved' in vals:
            if vals['qty_local_stock'] - vals['qty_reserved'] >= 0:
                return True
        elif 'qty_local_stock' in vals:
            if vals['qty_local_stock'] - pt.qty_reserved >= 0:
                return True
        elif 'qty_reserved' in vals:
            if pt.qty_local_stock - vals['qty_reserved'] >= 0:
                return True
        elif 'list_price' in vals:
            if pt.list_price != vals['list_price']:
                return True
        elif 'stock_cost' in vals:
            if pt.stock_cost != vals['stock_cost']:
                return True
        elif 'net_price' in vals:
            if pt.net_price != vals['net_price']:
                return True
        elif 'chrono24_price' in vals:
            if pt.chrono24_price != vals['chrono24_price']:
                return True
        return False


