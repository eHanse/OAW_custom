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


    net_price_usd = fields.Float(
        string='Sale USD',
        compute='_get_foreign_net_price',
        digits=dp.get_precision('Product Price')
    )
    net_price_chf = fields.Float(
        string='Sale CHF',
        compute='_get_foreign_net_price',
        digits=dp.get_precision('Product Price')
    )
    net_price_eur = fields.Float(
        string='Sale EUR',
        compute='_get_foreign_net_price',
        digits=dp.get_precision('Product Price')
    )

    @api.multi
    def _get_foreign_net_price(self):
        usd_rec = self.env['res.currency'].search([('name', '=', 'USD')])[0]
        chf_rec = self.env['res.currency'].search([('name', '=', 'CHF')])[0]
        eur_rec = self.env['res.currency'].search([('name', '=', 'EUR')])[0]
        for pt in self:
            if usd_rec:
                pt.net_price_usd = pt.net_price * usd_rec.rate_silent
            if chf_rec:
                pt.net_price_chf = pt.net_price * chf_rec.rate_silent
            if eur_rec:
                pt.net_price_eur = pt.net_price * eur_rec.rate_silent



