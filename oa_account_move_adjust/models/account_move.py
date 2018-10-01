'''
Created on 27 Apr, 2015

@author: roomsfor
'''

import openerp
from openerp.osv import fields, osv

class account_voucher_ext(osv.osv):
    _inherit = "account.move"



    def action_orders_3(self, cr, uid, ids, context=None):
        view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'account', 'view_move_form')[1]
        return {
            'name': 'Journal Entry',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'account.move',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'res_id': ids[0],
            'context': context,
        }