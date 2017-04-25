# -*- coding: utf-8 -*-
from openerp import models,fields,api
class PurchaseOrderLine(models.Model):
    #No need for sophisticated subclass
    #_name = 'purchase.order.ext'
    _inherit = 'purchase.order.line'
    _description = 'Traditional Inheritance on purchase.order.lines'
    #Relational Field unnecessary because there exists already one 
    #po_id = fields.Many2one('purchase.order', string='Purchase Order')
    #Related Field
    sup_ref = fields.Char(
        'Supplier Reference',
        related='order_id.partner_ref',
        readonly=True,
        store=True
    )

    