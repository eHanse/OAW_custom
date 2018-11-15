# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"




    @api.multi
    def updated_chrono24_date_button(self):
        for pt in self:
            pt.product_tmpl_id.updated_date_chrono24 = fields.Datetime.now()
            pt.product_tmpl_id.chrono24_updated = True

    @api.onchange('partner_offer_checked')
    def _onchange_partner_offer_checked(self):
        print('test 1')
        if self.partner_offer_checked:
            self.qty_down = False
            self.qty_up = False
            self.costprice_up = False
            self.costprice_down = False
            self.note_updated = False
