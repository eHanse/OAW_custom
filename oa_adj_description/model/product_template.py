# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ProductTemplateExt(models.Model):
    _inherit = 'product.template'
    @api.multi
    def write(self, vals):
        res = super(ProductTemplateExt, self).write(vals)
        if 'name' in vals:
            for pt in self:
                # Get the stock.transfer_details_items object
                transfer_details_items_object = self.env['stock.transfer_details_items']
                domain = [('product_id', 'in', pt.product_variant_ids.ids)]
                items = transfer_details_items_object.search(domain)
                for item in items:
                    item.sudo().write({'new_description': pt.name})

        return res







