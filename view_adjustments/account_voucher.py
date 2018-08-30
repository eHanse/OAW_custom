'''
Created on 27 Apr, 2015

@author: roomsfor
'''

import openerp
from openerp.osv import fields, osv


class account_voucher_line_ext(osv.osv):
    _inherit = "account_voucher.account_voucher_line"

    _columns = {
        'vouchers_sale_order':fields.related('move_line_id','ref', type='char', string='Sales Order', readonly=True, store=True),
        'customer_payment_reviewed': fields.boolean('Reviewed', readonly=True,store=True),
        'supplier_payment_reviewed': fields.boolean('Reviewed',readonly=True, store=True),
    }