# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # this field is added due to kanban view limitation
    # i.e. decimal place values cannot be eliminated by view adjustment

    local_stock_not_reserved = fields.Integer(
        string="Local Stock",
        compute="_get_local_stock_not_reserved",
        store=True,
        readonly=True,
    )


    @api.multi
    @api.depends('qty_local_stock', 'qty_reserved')
    def _get_local_stock_not_reserved(self):
        for pt in self:
            pt.local_stock_not_reserved = pt.qty_local_stock - pt.qty_reserved

