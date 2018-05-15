# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp



class ProductsSale (models.Model):
    _inherit = 'product.template'
    _description = 'Products Sale'

    total = fields.Float(
        string="Total",
        digits=dp.get_precision('Product Price'),
        readonly=True
    )

    average = fields.Float(
        string="Average Price",
        digits=dp.get_precision('Product Price'),
        readonly=True,
        compute='_calc_average'
    )

    counts = fields.Integer(
        "amount of sol",
        readonlu=True
    )
    @api.multi
    def _calc_average(self):
        for pt in self:
            if pt.counts != 0:
                pt.average = pt.total/pt.counts

    @api.multi
    def _initialize_values(self, pts):
        SOL = self.env['sale.order.line']
        Rate = self.env['res.currency.rate']
        for pt in pts:
            domain = [
                ('product_tmpl_id', '=', pt),
                ('state', '=', 'done'),
            ]
            sols = SOL.search(domain)
            sols_len = len(sols)
            if sols_len != 0:
                #Updating pt's sol count
                pt.counts = sols_len
                for sol in sols:
                    date = sol.order_id.date_order
                    rate = 1.0
                    if date and sol.order_id.currency_id != self.env.user.company_id.currency_id:
                        rate = Rate.search([
                            ('currency_id', '=', sol.order_id.currency_id.id),
                            ('name', '<=', date),
                        ], order='name desc', limit=1).rate or 1.0
                    sol.subtotal_hkd = sol.price_subtotal / rate
                    #Updating pt's total
                    pt.total =+ sol.subtotal_hkd

                #Updating pt's average
                pt.average = pt.total/pt.counts
        return


