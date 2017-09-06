

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    #For a filter in Product List Price Update view (tree) that bases on product.product
    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    #Product.Product listening to product_template
    # For a filter in Product and Product Offer views
    list_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    @api.multi
    @api.depends('product_tmpl_id.currency_price_change_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.currency_price_change_date = fields.Datetime.now()


    #Product.product listens to product.template because list_price belongs to product_template
    @api.multi
    @api.depends('product_tmpl_id.list_price_change_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.list_price_change_date = fields.Datetime.now()