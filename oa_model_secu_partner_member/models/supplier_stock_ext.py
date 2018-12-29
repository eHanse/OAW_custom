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

    sale_in_usd = fields.Float(
        string='Sale USD',
        compute='_get_sale_price_currency',
        digits=dp.get_precision('Product Price')
    )
    sale_in_eur = fields.Float(
        string='Sale EUR',
        compute='_get_sale_price_currency',
        digits=dp.get_precision('Product Price')
    )
    sale_in_chf = fields.Float(
        string='Sale CHF',
        compute='_get_sale_price_currency',
        digits=dp.get_precision('Product Price')
    )
    sale_in_rmb = fields.Float(
        string='Sale RMB',
        compute='_get_sale_price_currency',
        digits=dp.get_precision('Product Price')
    )

    @api.multi
    def _get_sale_price_currency(self):
        usd_rec = self.env['res.currency'].search([('name', '=', 'USD')])[0]
        eur_rec = self.env['res.currency'].search([('name', '=', 'EUR')])[0]
        chf_rec = self.env['res.currency'].search([('name', '=', 'CHF')])[0]
        rmb_rec = self.env['res.currency'].search([('name', '=', 'CNY')])[0]
        if usd_rec and eur_rec and chf_rec and rmb_rec:
            for st in self:
                st.sale_in_usd = st.price_unit_base * usd_rec.rate_silent
                st.sale_in_eur = st.price_unit_base * eur_rec.rate_silent
                st.sale_in_chf = st.price_unit_base * chf_rec.rate_silent
                st.sale_in_rmb = st.price_unit_base * rmb_rec.rate_silent

    @api.multi
    def write(self, vals):
        for ps in self:
            # For Special Price Filter
            if 'price_unit' in vals:
                if ps.price_unit > vals['price_unit']:
                    ps.partner_stock_special_offer = fields.Datetime.now()

            if 'quantity' in vals:
                    if ps.quantity < vals['quantity']:
                        ps.partner_stock_qty_new = fields.Datetime.now()
        return super(SupplierStock, self).write(vals)