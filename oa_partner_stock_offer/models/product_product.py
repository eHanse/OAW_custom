# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def _update_partner_stock_last_modified(self):
        for product in self:
            last_partner_stock = self.env['supplier.stock'].sudo().search([
                ('product_id', '=', product.id)
            ], order='last_update_date desc', limit=1)
            if last_partner_stock:
                product.sudo().write({
                    'partner_stock_last_modified': last_partner_stock.last_update_date
                })
