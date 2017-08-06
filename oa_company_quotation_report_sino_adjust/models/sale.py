# -*- coding: utf-8 -*-
from openerp import models, fields, osv
from openerp import workflow

class saleOrderExtended(models.Model):
    _inherit = 'sale.order'
    _description = 'Just extends sale order by adding a button to status bar'




    def print_quotation_sino(self, cr, uid, ids, context=None):
        '''
        This function prints the the quotation  and mark it as sent, so that we can see more easily the next step of the workflow
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        self.signal_workflow(cr, uid, ids, 'quotation_sent')
        return self.pool['report'].get_action(cr, uid, ids, 'oa_company_quotation_report_sino_adjust.report_sale_order_sino', context=context)
