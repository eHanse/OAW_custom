# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_qty(self, prod_tmpl_id):
        res = 0.0
        domain = (['product_tmp_id', '=', prod_tmpl_id])
        sols = self.search(domain)
        total = 0
        for sol in sols:
            sum = sum + sol.price_subtotal
        return sum
    #api.depends
    def _update_prod_tmpl_amount_sold(self):
        for sol in self:
            #Relational field
            prod_tmpl = sol.product_tmpl_id
            amount = self._get_qty(prod_tmpl.id)
            prod_tmpl.total = amount
        return
