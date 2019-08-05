# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def _get_stock_cost(self):
        res =  super(ProductTemplate, self)._get_stock_cost()
        for pt in self:
            if pt.stock_cost:
                pt.update_public_category()
                pt.website_published = True
                if not pt.partner_offer_checked:
                    if pt.default_code == 'CU006':
                        print pt.sale_hkd_ac
                        print pt.stock_cost
        return res


    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        for template in self:
            if template.qty_local_own_stock and template.qty_reserved:
                if template.qty_local_own_stock - template.qty_reserved == 0:
                    if template.qty_local_supplier_stock and template.qty_overseas:
                        if template.qty_local_supplier_stock == 0.0 and template.qty_overseas == 0.0:
                            self.sale_hkd_ac = 0.0
        return res