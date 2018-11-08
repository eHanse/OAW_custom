# -*- coding: utf-8 -*-

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
                stock.product_id.product_tmpl_id.sudo().write({
                    'currency_price_change_date': fields.Datetime.now()
                })
        res = super(SupplierStock, self).write(vals)
        return res

    def check_changes(self, vals):
        pt = self.product_id.product_tmpl_id
        if 'quantity' in vals:
            curr_quantity = self.quantity
            if curr_quantity < vals['quantity']:
                pt.sudo().write({'qty_up': True, 'partner_offer_checked': False})
            elif curr_quantity > vals['quantity']:
                pt.sudo().write({'qty_down': True, 'partner_offer_checked': False})
        if 'price_unit' in vals:
            curr_price_unit = self.price_unit
            if curr_price_unit < vals['price_unit']:
                pt.sudo().write({'costprice_up': True, 'partner_offer_checked': False})
            elif curr_price_unit > vals['price_unit']:
                pt.sudo().write({'costprice_down': True, 'partner_offer_checked': False})
        if 'partner_note' in vals:
            pt.sudo().write({'note_updated': True})

    @api.multi
    def write(self, vals):
        for ps in self:
            ps.check_changes(vals)
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
                    product_ref[0].product_tmpl_id.sudo().write({
                        'new_entry_date': fields.Datetime.now()
                    })
            # For Purchase Price Unit filter
            else:
                # Purchase price unit change
                if last_added_stock[0].price_unit != vals['price_unit']:
                    vals['currency_price_change_date'] = fields.Datetime.now()
                    last_added_stock[0].product_id.product_tmpl_id.sudo().write({
                        'currency_price_change_date': fields.Datetime.now()
                    })
                # For New Entry filter : New Stock with same price but maybe different supplier
                else:
                    vals['new_entry_date'] = fields.Datetime.now()
                    last_added_stock[0].product_id.product_tmpl_id.sudo().write({
                        'new_entry_date': fields.Datetime.now()
                    })
        res = super(SupplierStock, self).create(vals)
        return res

