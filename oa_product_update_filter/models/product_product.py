

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    # For a filter in Product List Price Update view (tree) that bases on product.product
    currency_price_change_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # For a filter in List Price Update
    list_price_change_date = fields.Datetime(
        string="Update listprice, HKD Retail",
        store=True,
    )

    # For a filter in Product and Product Offer
    # Trigger: product_template.new_entry_date
    new_entry_date = fields.Datetime(
        string="Update Currency Amount Price",
        store=True,
    )

    # Field for filter showing increase of net_price during the last 24h in Listprice Update
    # Update triggered by product_template's field change
    price_up_date = fields.Datetime(
        string="Sale HKD went up",
        store=True,
    )
    # Field for filter showing decrease of net_price during the last 24h in Listprice Update
    # Update triggered by product_template's field change
    price_down_date = fields.Datetime(
        string="Sale HKD went down",
        store=True,
    )

    # Updates currency_price_change_date
    @api.multi
    @api.depends('product_tmpl_id.currency_price_change_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.currency_price_change_date = fields.Datetime.now()


    # Updates list_price_change_date
    # Assumption: If this method is triggered, self contains all records whose list_price had been change.
    # Which can be only one in a time.
    @api.multi
    @api.depends('product_tmpl_id.list_price_change_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.list_price_change_date = fields.Datetime.now()

    # Updates new_entry_date
    @api.multi
    @api.depends('product_tmpl_id.new_entry_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.list_price_change_date = fields.Datetime.now()

    # All products of certain product_tmpl_id are updated
    @api.multi
    @api.depends('product_tmpl_id.price_up_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.price_up_date = fields.Datetime.now()
            # Updates new_entry_date

    # All products of certain product_tmpl_id are updated
    @api.multi
    @api.depends('product_tmpl_id.price_down_date')
    def update_updated_price_change_date(self):
        for p in self:
            p.price_down_date = fields.Datetime.now()