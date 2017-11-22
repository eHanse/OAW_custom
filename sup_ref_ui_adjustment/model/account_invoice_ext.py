# -*- coding: utf-8 -*-
from openerp import models, fields, api


class OnDraftInvoices(models.Model):

    _inherit = 'account.invoice'
    _description = 'Trying to get partner_ref into account.invoice.tree'


    # overwrite write() for updating PO for showing sup ref there
    @api.multi

    def write(self, vals):
        if 'supplier_invoice_number' in vals:
            for ai in self:
                #in-invoice = supplier invoice
                if ai.type == 'in_invoice':
                    for inv_line in ai.invoice_line:
                        inv_line.po_id.partner_ref = vals['supplier_invoice_number']
        res = super(OnDraftInvoices, self).write(vals)
        return res





