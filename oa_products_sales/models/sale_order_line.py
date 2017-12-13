# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    #products_sales_qty = fields.Integer(string="Qty of sales of a product")


    @api.multi
    def _get_amount(self, prod_tmpl_id):
        amount = 0.0
        domain = [
            ('product_tmpl_id', '=', prod_tmpl_id),
            ('state','=', 'done'),
        ]
        sols = self.search(domain)
        sols_len = len(sols)
        if sols_len != 0:
                for sol in sols:
                    amount = amount + sol.price_subtotal
        else:
             amount =0
             sols_len = 1

        res = [amount,sols_len]
        return res

    @api.multi
    def _update_prod_tmpl_amount_and_average(self):
        for sol in self:
            # Relational field
            prod_tmpl = sol.product_tmpl_id
            res = self._get_amount(prod_tmpl.id)
            prod_tmpl.total = res[0]
            prod_tmpl.average = res[0]/res[1]
        return

    # Will be executed whenever quotation is confirmed. The sol of the quotation exists already by then.
    # That is why sols of newly created quotation are considered when _update_prod_tmpl.... function is called.
    @api.multi
    def write(self, vals):
        res = super(SaleOrderLine, self).write(vals)
        self._update_prod_tmpl_amount_and_average()
        return res

