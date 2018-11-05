# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
from datetime import timedelta as td
from openerp.fields import Date as fDate


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # this field is added due to kanban view limitation
    # i.e. decimal place values cannot be eliminated by view adjustment

    internal_stock = fields.Integer(
        string="Stock",
        compute="_get_internal_stock",
        store=True,
        readonly=True,
    )

    internal_stock_available = fields.Char(
        string="Available",
        compute="_get_internal_stock_avail",
        readonly=True,
    )

    internal_stock_change = fields.Datetime(
        compute='update_internal_stock_date',
        store=True,
        string="Internal Stock Update",
    )

    list_price_special_date = fields.Datetime(
        store=True,
        string="Special Offer",
    )
    list_price_special = fields.Boolean(
        compute='update_list_price_special',
        string="Inernal Stock Update",
        default = False
    )

    @api.multi
    def update_list_price_special(self):
        for pt in self:
            now = fields.Datetime.now()
            special_date = pt.list_price_special_date
            if special_date:
                delta = now-special_date
                if delta.seconds < 86400 :
                    pt.list_price_special = True
                else:
                    pt.list_price_special = False
            else :
                pt.list_price_special = False
                print pt.list_price_special

    @api.multi
    @api.depends('internal_stock_available')
    def update_internal_stock_date(self):
        for pt in self:
            pt.internal_stock_change = fields.Datetime.now()
    @api.multi
    @api.depends('local_stock_not_reserved', 'qty_overseas')
    def _get_internal_stock(self):
        for pt in self:
            pt.internal_stock = pt.local_stock_not_reserved + pt.qty_overseas


    def _get_internal_stock_avail(self):
        for pt in self:
            if pt.internal_stock > 0:
                pt.internal_stock_available = 'Yes'
            else:
                pt.internal_stock_available = 'No'


    @api.multi
    def write(self, vals):
        for pt in self:
            if 'list_price' in vals:
                if pt.list_price > vals['list_price']:
                    pt.list_price_special_date = fields.Datetime.now()

        return super(ProductTemplate, self).write(vals)
