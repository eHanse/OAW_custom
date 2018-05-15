# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    subtotal_hkd = fields.Float(
        string="Subtotal in HKD",
        digits=dp.get_precision('Product Price'),
        readonly=True,
        store=True
    )

    @api.multi
    def _update_prod_tmpl_amount_and_average(self):
        for sol in self:
            Rate = self.env['res.currency.rate']

            date = sol.order_id.date_order
            rate = 1.0
            if date and sol.order_id.currency_id != self.env.user.company_id.currency_id:
                rate = Rate.search([
                    ('currency_id', '=', sol.order_id.currency_id.id),
                    ('name', '<=', date),
                ], order='name desc', limit=1).rate or 1.0
            sol.subtotal_hkd = sol.price_subtotal / rate
            # amount = amount + sol.price_subtotal / rate
            # Relational field
            sol.product_id.product_tmpl_id.total += sol.subtotal_hkd
            sol.product_id.product_tmpl_id.counts += 1


    # Will be executed whenever quotation is confirmed. The sol of the quotation exists already by then.
    # That is why sols of newly created quotation are considered when _update_prod_tmpl.... function is called.
    @api.multi
    def write(self, vals):
        if 'state' in vals and vals['state']=='done':
            self._update_prod_tmpl_amount_and_average()
        res = super(SaleOrderLine, self).write(vals)
        return res

