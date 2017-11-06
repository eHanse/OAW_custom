#
#
# from openerp import models, fields, api
#
#
# class ProductProduct(models.Model):
#     _inherit = "product.product"
#
#     # For a filter in Product List Price Update view (tree) that bases on product.product
#     currency_price_change_date = fields.Datetime(
#         related="product_tmpl_id.currency_price_change_date",
#     )
#
#     list_price_change_date = fields.Datetime(
#         related="product_tmpl_id.list_price_change_date",
#     )
#     # For a filter in Product and Product Offer
#     # Trigger: product_template.new_entry_date
#     new_entry_date = fields.Datetime(
#         related="product_tmpl_id.new_entry_date",
#     )
#
#     # Field for filter showing increase of net_price during the last 24h in Listprice Update
#     # Update triggered by product_template's field change
#     price_up_date = fields.Datetime(
#         related="product_tmpl_id.price_up_date",
#     )
#     # Field for filter showing decrease of net_price during the last 24h in Listprice Update
#     # Update triggered by product_template's field change
#     price_down_date = fields.Datetime(
#         related="product_tmpl_id.price_down_date",
#     )