# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = "product.template"



    @api.multi
    def write(self, vals):
        if 'partner_offer_checked' in vals:
            if vals['partner_offer_checked']:
                self.update_public_category()
                print("Updated")
                self.website_published = True
                print("Published")

        res = super(ProductTemplate, self).write(vals)
        return res