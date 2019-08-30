# -*- coding: utf-8 -*-
from openerp import models,fields,api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Modified description field for RFQ'

    new_description = fields.Char(
        related='product_id.name',
        string="Product Ref",
        readonly=True,
        store=True,
    )

    default_code = fields.Char(
        related='product_id.default_code',
        string='Code',
        readonly=True,
        store=True
    )

