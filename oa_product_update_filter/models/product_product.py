# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    # updated_chrono24 = fields.Datetime(
    #     related='product_tmpl_id.updated_chrono24',
    #     store=True,
    # )

    # Method triggered by UI
    # For chrono24 notice
    # @api.multi
    # def updated_chrono24_date_button(self):
    #     for p in self:
    #         p.product_tmpl_id.updated_chrono24 = fields.Datetime.now()