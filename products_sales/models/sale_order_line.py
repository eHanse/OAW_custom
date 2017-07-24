# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _get_amount(self, prod_tmpl_id):
        amount = 0.0
        domain = [
            ('product_tmpl_id', '=', prod_tmpl_id),
            ('state','=', 'sent'),
        ]
        sols = self.search(domain)
        for sol in sols:
            amount = amount + sol.price_subtotal
        return amount

    @api.multi
    def _update_prod_tmpl_amount_sold(self):
        for sol in self:
            # Relational field
            prod_tmpl = sol.product_tmpl_id
            amount = self._get_amount(prod_tmpl.id)
            prod_tmpl.total = amount
        return

    @api.multi
    def write(self, vals):
        res = super(SaleOrderLine, self).write(vals)
        self._update_prod_tmpl_amount_sold()
        return res

    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id, u"%s %s" % (record.product_tmpl_id.name, record.product_tmpl_id.default_code))
            )
        return result