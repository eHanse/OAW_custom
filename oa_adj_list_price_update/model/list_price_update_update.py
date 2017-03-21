# -*- coding: utf-8 -*-
from openerp import models,fields,api
import openerp.addons.decimal_precision as dp
#from pycparser.c_ast import Default
class list_price_update_update(models.Model):
    #No need for sophisticated subclass
    #_name = 'purchase.order.ext'
    _inherit = 'product.template'
    _description = 'Traditional Inheritance'


    discount = fields.Float(
        string="Discount (%)",
        digits=dp.get_precision('Discount'),
        compute='_compute_disc',
        readonly=True,
        store=True
    )

    net_profit = fields.Float(
        string="Net Profit",
        digits=dp.get_precision('Product Price'),
        compute='_compute_net_profit',
        readonly=True,
        store = True
    )

    net_profit_pct = fields.Float(
        string="Net Profit Percental",
        digits=dp.get_precision('Discount'),
        compute='_compute_net_profit_pct',
        readonly=True
    )

    last_in_date = fields.Date(
        string="Last Incoming Date",
        readonly=True,
        store=True
    )


    @api.multi
    @api.depends('net_price','list_price')
    def _compute_disc(self):
        for entry in self:
            if not entry.list_price:
                entry.discount = 0.0
            elif entry.net_price == 0.0:
                entry.discount = 0.0
            else:
                entry.discount = (1 - entry.net_price/entry.list_price) * 100
        return

    @api.multi
    @api.depends('net_price', 'stock_cost')
    def _compute_net_profit(self):
        for entry in self:
            if entry.net_price == 0.0 or entry.stock_cost == 0.0:
                entry.net_profit = 0.00
            else:
                entry.net_profit = entry.net_price - entry.stock_cost
        return

    @api.multi
    @api.depends('net_price', 'stock_cost')
    def _compute_net_profit_pct(self):
        for entry in self:
            if entry.net_price == 0.0 or entry.stock_cost == 0.0:
                entry.net_profit = 0.0
            else:
                entry.net_profit_pct = (entry.net_price/entry.stock_cost)*100-100
        return