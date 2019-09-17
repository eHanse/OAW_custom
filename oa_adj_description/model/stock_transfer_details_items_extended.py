# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockTransferDetailsItems(models.TransientModel):

    _inherit = 'stock.transfer_details_items'
    _description = 'Adjust Description field in all Transfer views'

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





