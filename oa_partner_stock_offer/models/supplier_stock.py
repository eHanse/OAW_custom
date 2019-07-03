# -*- coding: utf-8 -*-
# Copyright 2017-2019 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class SupplierStock(models.Model):
    _inherit = "supplier.stock"
    # Using "display_name" field computed by name_get() method to create the form view's representation
    _rec_name = 'display_name'

    # Field to access through related field: Supplier.Stock > Product.Product > Product.Template
    # hk_retail = fields.Float(
    #     'Retail HKD',
    #      related='product_id.list_price',
    #      store=True,
    # )
    # quantity, computed field
    partner_qty = fields.Char(
        string='Evaluated Quantity',
        store=True,
    )
    # Cheapest entry of product_id?
    lowest_cost = fields.Boolean(
        string='Cheapest entry',
        store=True,
    )
    # Flags those ps that have multiple entries with same product_id
    has_duplicates = fields.Boolean(
        string='Has Duplicates',
        store=True,
    )
    # For form view
    image_medium = fields.Binary(
        'Image',
        related='product_id.product_tmpl_id.image_medium',
        readonly=True,
    )
    short_loc_name = fields.Char(
        "Location",
        related='partner_loc_id.short_loc')
    brand = fields.Char(
        related='prod_cat_selection.name',
        string='Brand',
    )
    last_update_date = fields.Datetime(
        readonly=True,
        string='Last Update Date'
    )
    last_update_user_id = fields.Many2one(
        'res.users',
        readonly=True,
        string='Last Update User',
    )
    # For new Filter in Partner Stock
    # For Partner Stock filter
    qty_up_date = fields.Datetime(
        string='Quantity increased',
        store=True
    )
    qty_down_date = fields.Datetime(
        string='Quantity decreased',
    )
    costprice_up_date = fields.Datetime(
        string='Costprice increased',
        readonly=True,
    )
    costprice_down_date = fields.Datetime(
        string='Costprice decreased',
        readonly=True,
    )
    note_updated_date = fields.Datetime(
        string='Partner Note updated',
    )

    @api.multi
    def _get_quantity(self):
        for ps in self:
            if ps.quantity == 0.0:
                ps.partner_qty = '0'
            elif ps.quantity == 1.0:
                ps.partner_qty = '1'
            elif ps.quantity == 2.0:
                ps.partner_qty = '2'
            elif ps.quantity >= 3.0:
                ps.partner_qty = '>=3'
            ps_products = self.sudo().search(
                [('product_id', '=', ps.product_id.id)], order='price_unit_base ASC'
            )
            if ps_products:
                for psc in ps_products:
                    if len(ps_products) >= 2:
                        psc.sudo().write({
                            'lowest_cost': False,
                            'has_duplicates': True
                        })
                    else:
                        psc.sudo().write({
                            'lowest_cost': False,
                            'has_duplicates': False,
                        })
                ps_products[0].sudo().write({
                    'lowest_cost': True
                })

    @api.multi
    def write(self, vals):
        if 'quantity' in vals or 'price_unit' in vals or 'partner_loc_id' in vals or 'prod_cat_selection' in vals \
                or 'product_id' in vals or 'currency_id' in vals or 'retail_in_currency' in vals or 'partner_note' in vals:
            vals.update({
                'last_update_date': fields.Datetime.now(),
                'last_update_user_id': self.env.user.id
            })
            for ps in self:
                ps.product_id.product_tmpl_id.sudo().write(
                    {'partner_stock_last_modified': fields.Datetime.now()})
                if 'quantity' in vals:
                    if ps.quantity < vals['quantity']:
                        ps.qty_up_date = fields.Datetime.now()
                    if ps.quantity > vals['quantity']:
                        ps.qty_down_date = fields.Datetime.now()
                if 'price_unit' in vals:
                    if ps.price_unit < vals['price_unit']:
                        ps.costprice_up_date = fields.Datetime.now()
                    if ps.price_unit > vals['price_unit']:
                        ps.costprice_down_date = fields.Datetime.now()
                if 'partner_note' in vals:
                    ps.note_updated_date = fields.Datetime.now()
        res = super(SupplierStock, self).write(vals)
        for ps in self:
            if 'quantity' in vals:
                ps._get_quantity()
        return res

    @api.model
    def create(self, vals):
        vals.update({
            'last_update_date': fields.Datetime.now(),
            'last_update_user_id': self.env.user.id
        })
        self.env['product.product'].browse(vals['product_id']).product_tmpl_id.sudo(
        ).write({'partner_stock_last_modified': fields.Datetime.now()})
        res = super(SupplierStock, self).create(vals)
        res._get_quantity()
        return res

    @api.multi
    def unlink(self):
        product_ids = []
        for ps in self:
            product_ids.append(ps.product_id.id)
        res = super(SupplierStock, self).unlink()
        related_ps = self.search([('product_id', 'in', product_ids)])
        if related_ps:
            related_ps._get_quantity()
        return res
