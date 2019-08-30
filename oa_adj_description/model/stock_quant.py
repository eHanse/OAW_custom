# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockQuantExtended(models.Model):

    _inherit = 'stock.quant'
    _description = 'Adjust Description field in form Views of Tree'

    new_description = fields.Char(
        related='product_id.name',
        string="Product Ref",
        readonly=True,
        store=True,
    )

    default_code = fields.Char(
        related ='product_id.default_code',
        string = 'Code',
        readonly = True,
        store = True
    )




