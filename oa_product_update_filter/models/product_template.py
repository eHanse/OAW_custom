# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    updated_c24_date = fields.Datetime(
        string="Updated C24 Date",
        store=True,
    )

    product_id = fields.Integer(
        string='product_id',
        compute='_get_product',
    )


    @api.multi
    def _get_product(self):
        rec = self.env['product.product'].search([('id', '=', 'product_tmpl_id')])[0]
        if rec:
            for pt in self:
                pt.product_id = rec.id

