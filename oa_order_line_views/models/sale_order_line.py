# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
from datetime import datetime, timedelta


class SaleOrderLineExt(models.Model):
    _inherit = "sale.order.line"
    #
    is_mto = fields.Boolean(
        string='MTO',
        related='order_id.is_mto',
    )
    product_code = fields.Char(
        related='product_id.code',
        string="Code",
        store=True
    )
    product_name = fields.Char(
        related='product_id.name',
        string="Product",
        store=True
    )
    order_price_list = fields.Char(
        related='order_id.pricelist_id.name',
        string="Price List",
    )
    order_date = fields.Datetime(
        related='order_id.date_order',
        string="Date",
    )

    supplier_code = fields.Char(
        'Supplier Code',
        related='order_id.supplier_code',
        store=True
    )
    supplier_note = fields.Char(
        'Supplier Notes',
    )
    sales_remark = fields.Char(
        'Sales Team Remark'
    )



