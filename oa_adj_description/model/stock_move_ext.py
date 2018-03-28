# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockMovesExt(models.Model):

    _inherit = 'stock.move'
    _description = 'Adjust Description field in form Views of Tree and Form views'

    new_description = fields.Char(
        related='product_id.product_tmpl_id.name',
        string="Description",
        readonly=True,
        store=True,
    )





