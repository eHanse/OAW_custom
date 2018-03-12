# -*- coding: utf-8 -*-
from openerp import models,fields,api
class PurchaseOrderLine(models.Model):


    _inherit = 'purchase.order.line'
    _description = 'Via related field provides underlying Purchase Order with supplier reference)'

    sup_ref = fields.Char(
        'Supplier Reference',
        related='order_id.partner_ref',
    )

    new_description = fields.Char(
        related='product_id.product_tmpl_id.name',
        string="Description",
        readonly=True
    )


