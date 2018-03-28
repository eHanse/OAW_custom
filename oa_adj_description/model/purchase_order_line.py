# -*- coding: utf-8 -*-
from openerp import models,fields,api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Modified description field for RFQ'

    new_description = fields.Char(
        related='product_id.product_tmpl_id.name',
        string="Description",
        readonly=True,
        store=True,
    )


