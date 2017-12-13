# -*- coding: utf-8 -*-


from openerp import models, fields, api



class StockQuant(models.Model):
    _inherit = 'stock.quant'

   # For filter New Entry 24
    @api.model
    def create(self, vals):
        # For Filter: New Entry 24h
        domain = [
            ('id', '=', vals['product_id']),
        ]
        product_ref = self.env['product.product'].search(domain, order='create_date DESC', limit=1)
        product_ref.product_tmpl_id.new_entry_date = fields.Datetime.now()
        return super(StockQuant, self).create(vals)

