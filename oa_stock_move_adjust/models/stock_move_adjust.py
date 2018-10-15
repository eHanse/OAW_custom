# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockMoveExtended(models.Model):

    _inherit = 'stock.move'

    source_document = fields.Char(
        'Source Document',
        related = 'picking_id.origin'
    )






