# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    subtotal_hkd = fields.Float(
        string="Subtotal in HKD",
        digits=dp.get_precision('Product Price'),
        readonly=True
    )

    @api.multi
    def _get_amount(self, prod_tmpl_id):
        amount = 0.0
        domain = [
            ('product_tmpl_id', '=', prod_tmpl_id),
            ('state','=', 'done'),
        ]
        # SOLs with identical products
        sols = self.search(domain)
        sols_len = len(sols)
        if sols_len != 0:
            # We need the rate of the day of the confirmed Sales Order (in OA that date is relevant, not invoice date)
            Rate = self.env['res.currency.rate']
            for sol in sols:
                date = sol.order_id.date_order
                if date:
                    rate = Rate.search([
                        ('currency_id', '=', sol.order_id.currency_id.id),
                        ('name', '<=', date),
                    ], order='name desc', limit=1).rate or 1.0
                subtotal_hkd = sol.price_subtotal / rate
                amount = amount + sol.price_subtotal / rate
        else:
             amount =0
             sols_len = 1

        res = [amount,sols_len,subtotal_hkd ]
        return res

    @api.multi
    def _update_prod_tmpl_amount_and_average(self):
        for sol in self:
            # Relational field
            prod_tmpl = sol.product_tmpl_id
            res = self._get_amount(prod_tmpl.id)
            prod_tmpl.total = res[0]
            prod_tmpl.average = res[0]/res[1]

        return res[2]

    # Will be executed whenever quotation is confirmed. The sol of the quotation exists already by then.
    # That is why sols of newly created quotation are considered when _update_prod_tmpl.... function is called.
    @api.multi
    def write(self, vals):
        subtotal_hkd = self._update_prod_tmpl_amount_and_average()
        vals['subtotal_hkd'] = subtotal_hkd
        res = super(SaleOrderLine, self).write(vals)
        return res

