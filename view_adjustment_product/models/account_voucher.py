'''
Created on 27 Apr, 2015

@author: roomsfor
'''

import openerp
from openerp.osv import fields, osv


class account_voucher_line_ext(osv.osv):
    _inherit = "account.voucher.line"

    _columns = {
        'vouchers_lines_ref': fields.related('move_line_id', 'ref', type='char', string='Sales Order', readonly=True, store=True),

    }

class account_voucher_ext(osv.osv):
    _inherit = "account.voucher"

    _columns = {
        'vouchers_sales_order': fields.char(type='char', string='Sales Order', readonly=True,store=True),
        'voucher_payment_reviewed': fields.boolean('Payment Reviewed', store=True),
    }



    def get_vouchers_sale_order(self, cr, uid, ids, context=None):
        voucher_lines = self.pool.get('account.voucher.line')
        for this in self.browse(cr, uid, ids, context=context):
            voucher_lines_ids = voucher_lines.search(cr, uid,
                [('voucher_id', '=', this.id),
                 ('vouchers_lines_ref', 'like', 'SO%')
                 ],context=context

            )
            if voucher_lines_ids:
                voucher_line_id = voucher_lines.browse(cr, uid, voucher_lines_ids, context=context)[0]
                this.vouchers_sales_order = voucher_line_id.vouchers_lines_ref


    def create(self, cr, uid, vals, context=None):
        res = super(account_voucher_ext,self).create(cr, uid, vals, context=context)
        self.get_vouchers_sale_order(cr, uid, [res], context=context)
        return res


    def action_orders_2(self, cr, uid, ids, context=None):
        view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'account_voucher', 'view_vendor_receipt_form')[1]
        return {
            'name': 'Customer Payments',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'account.voucher',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'res_id': ids[0],
            'context': context,
        }