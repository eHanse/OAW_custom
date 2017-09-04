

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    @api.multi
    @api.depends('product_tmpl_id.currency_price_change_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.currency_price_change_date = fields.Datetime.now()