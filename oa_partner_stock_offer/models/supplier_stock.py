# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class SupplierStock(models.Model):
    _inherit = "supplier.stock"

    # Field to access through related field: Supplier.Stock > Product.Product > Product.Template
    hk_retail = fields.Float(
        'Retail HKD',
         related='product_id.list_price',
         store=True,
    )
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
    image_medium = fields.Binary(
        'Image',
        related='product_id.product_tmpl_id.image_medium',
        readonly=True,
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
            ps_products= self.sudo().search(
                [('product_id', '=', ps.product_id.id)], order='price_unit_base ASC'
            )
            if ps_products:
                for psc in ps_products:
                    if len(ps_products) >=2:
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
        res = super(SupplierStock, self).write(vals)
        if 'quantity' in vals or 'price_unit' in vals:
            for ps in self:
                ps._get_quantity()
        return res

    @api.model
    def create(self,vals):
        res =super(SupplierStock,self).create(vals)
        res._get_quantity()
        return res