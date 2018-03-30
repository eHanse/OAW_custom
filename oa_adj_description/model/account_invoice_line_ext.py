# -*- coding: utf-8 -*-
from openerp import models, fields, api


class OnDraftInvoices(models.Model):

    _inherit = 'account.invoice.line'
    _description = 'Adjust Description field in "On Draft Invoices"'

    new_description = fields.Char(
        related='product_id.product_tmpl_id.name',
        string="Description",
        readonly=True,
        store=True,
    )





