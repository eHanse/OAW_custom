# -*- coding: utf-8 -*-
from openerp import models, fields, api


class OnDraftInvoices(models.Model):

    _inherit = 'account.invoice.line'
    _description = 'Adjust Description field in "On Draft Invoices"'

    new_description = fields.Char(
        related='product_id.name',
        string="Product Ref",
        readonly=True,
        store=True,
    )

    default_code = fields.Char(
        related ='product_id.default_code',
        string = 'Code',
        readonly = True,
        store = True
    )





