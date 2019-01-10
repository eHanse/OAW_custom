# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp


class SupplierStock(models.Model):
    _inherit = 'supplier.stock'

    partner_stock_special_offer = fields.Datetime(
        store=True,
        string="Special Offer",
    )

    partner_stock_qty_new = fields.Datetime(
        store=True,
        string="Qty Changed",
    )


    @api.multi
    def write(self, vals):
        for ps in self:
            # For Special Price Filter
            if 'price_unit' in vals:
                if ps.price_unit > vals['price_unit']:
                    ps.partner_stock_special_offer = fields.Datetime.now()

            if 'quantity' in vals:
                if ps.quantity == 0.0:
                    if ps.quantity < vals['quantity']:
                        ps.partner_stock_qty_new = fields.Datetime.now()
        return super(SupplierStock, self).write(vals)