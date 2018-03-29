# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockQuantExtended(models.Model):

    _inherit = 'stock.quant'
    _description = 'Adjust Description field in form Views of Tree'

    new_description = fields.Char(
        related='product_id.product_tmpl_id.name',
        string="Description",
        readonly=True,
        store=True,
    )





