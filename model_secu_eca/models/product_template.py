# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
from datetime import datetime, timedelta as td
from openerp.fields import Date as fDate


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # this field is added due to kanban view limitation
    # i.e. decimal place values cannot be eliminated by view adjustment

    internal_stock = fields.Integer(
        string="Stock",
        compute = '_get_internal_stock',
        store=True,
        readonly=True,
    )
    internal_stock_available = fields.Char(
        string="Available",
        compute="_get_internal_stock",
        readonly=True,
        store = True,
    )
    internal_stock_change_date = fields.Datetime(
        store=True,
        string="Internal Stock Update",
    )
    list_price_special_date = fields.Datetime(
        store=True,
        string="Special Offer",
    )

    brand = fields.Char(
        'Brand',
        related = 'categ_id.name',
        store = True
    )



    @api.multi
    @api.depends('local_stock_not_reserved', 'qty_overseas')
    def _get_internal_stock(self):
        for pt in self:
            pt.internal_stock = pt.local_stock_not_reserved + pt.qty_overseas
            if pt.internal_stock > 0:
                pt.internal_stock_available = 'Yes'
            else:
                pt.internal_stock_available = 'No'


    @api.multi
    def write(self, vals):
        for pt in self:
            # For Special Price Filter
            if 'net_price' in vals:
                if pt.net_price > vals['net_price']:
                    pt.list_price_special_date = fields.Datetime.now()
            if 'sale_hkd_aa_so' in vals:
                if pt.sale_hkd_aa_so > vals['sale_hkd_aa_so']:
                    pt.list_price_special_date = fields.Datetime.now()
            if 'sale_hkd_ac' in vals:
                if pt.sale_hkd_ac > vals['sale_hkd_ac']:
                    pt.list_price_special_date = fields.Datetime.now()
            # For New Arrival Filter
            if 'qty_local_stock' in vals and 'qty_reserved' in vals:
                if pt.qty_local_stock + pt.qty_reserved < vals['qty_local_stock'] + vals['qty_reserved']:
                    pt.internal_stock_change_date = fields.Datetime.now()
            if 'qty_local_stock' in vals:
                if pt.qty_local_stock < vals['qty_local_stock']:
                    pt.internal_stock_change_date = fields.Datetime.now()
            if 'qty_overseas' in vals:
                if pt.qty_overseas < vals['qty_overseas']:
                    pt.internal_stock_change_date = fields.Datetime.now()
        return super(ProductTemplate, self).write(vals)
