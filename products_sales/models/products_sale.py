# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp



class ProductsSale (models.Model):
    _inherit = 'product.template'
    _description = 'Products Sale'
    name = fields.Char('Title', required=True)

    total = fields.Float(
        string="Total",
        digits=dp.get_precision('Product Price'),
        readonly=True
    )

    #Computes the total sale for each product.
    #Problem: if not using store=True, this method time-consuming method will always be called
    #Problem: if using store=True the values are "0"
    #api.depends might be the solution, first of all that it looks for changes even in other models then self.
    #@api.depends('')

   # def _get_total(self):
     #   sols = self.env['sale.order.line']
     #   for pt in self:
     #       domain = [('product_tmpl_id', '=', pt.id)]
    #        rel_sols = sols.search(domain)
     #       if rel_sols:
     #           sum = 0
      #          for sol in rel_sols:
        #            sum = sum + sol.price_subtotal
        #        pt.total = sum





