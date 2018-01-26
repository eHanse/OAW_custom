# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class SupplierStock(models.Model):
    _inherit = "supplier.stock"

    # Field to access through related field: Supplier.Stock > Product.Product > Product.Template
    hk_retail = fields.Float(
        'HK Retail',
         related='product_id.list_price',
         store=True,
    )
    # quantity, computed field
    partner_quantity = fields.Char(
        string='Quantity',
        store=True,
    )

    # Cheapest entry of product_id?
    cheapest = fields.Boolean(
        string='Cheapest entry',
        store=True,
    )



    @api.multi
    def _get_quantity(self):
        for ps in self:
            if ps.quantity == 0.0:
                ps.partner_quantity = '0'
            elif ps.quantity == 1.0:
                ps.partner_quantity = '1'
            elif ps.quantity == 2.0:
                ps.partner_quantity = '2'
            elif ps.quantity >= 3.0:
                ps.partner_quantity = '>=3'
            ps_products= self.search(
                [('product_id', '=', ps.product_id.id)], order='price_unit_base ASC'
            )
            if ps_products:
                for psc in ps_products:
                        psc.cheapest = False
                ps_products[0].cheapest = True

    @api.multi
    def write(self, vals):
        for ps in self:
            ps._get_quantity()
        return super(SupplierStock, self).write(vals)