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

    subtotal_sold = fields.Float(
        string="Total"
    )








