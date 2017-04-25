# -*- coding: utf-8 -*-
from openerp import models,fields,api
class PurchaseOrderLine(models.Model):
    #No need for sophisticated subclass
    #_name = 'purchase.order.ext'
    _inherit = 'purchase.order.line'
    _description = 'Traditional Inheritance on purchase.order.lines'

    image_small = fields.Binary(
        'Image',
        related='product_id.product_tmpl_id.image_small',
        readonly=True
    )
  

    