# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ProductTemplateExt(models.TransientModel):

    @api.multi
    def write(self, vals):
        res = super(ProductTemplateExt, self).write(vals)
        if 'name' in vals:
            for pt in self:
                #Get the stock.transfer_details_items object
                transfer_details_items_object = self.env['stock.transfer_details_items']
                domain = [('product_id', '=', pt.id)]
                transfer_details_items_object.search(domain)
                for item in transfer_details_items_object:
                    item.sudo().write({'new_description': pt.name})





