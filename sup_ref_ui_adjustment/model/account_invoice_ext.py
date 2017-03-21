# -*- coding: utf-8 -*-
from openerp import models, fields, api


class OnDraftInvoices(models.Model):
    # No need for sophisticated subclass
    # _name = 'purchase.order.ext'
    _inherit = 'account.invoice'
    _description = 'Trying to get partner_ref into account.invoice.tree'
    # Relational Field unnecessary because there exists already one
    # po_id = fields.Many2one('purchase.order', string='Purchase Order')
    # Related Field
    partner_ref = fields.Char(
        'Supplier Reference',
        compute='_get_partner_ref',
        readonly=True,
        store=True
    )

    @api.multi
    def _get_partner_ref(self):
        for ai in self:
            ai.partner_ref = self.env['purchase.order'].search([('origin', '=', 'ai.origin')])




