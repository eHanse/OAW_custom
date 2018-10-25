# -*- coding: utf-8 -*-
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp



class SaleOrderExt (models.Model):
    _inherit = 'sale.order'
    _description = 'Adding Sales Supplier'


    supplier_id = fields.Many2one(
        comodel_name='res.partner',
        string="Sales Supplier",
        store=True
        # default = lambda self: self.env.user.partner_id
    )
    supplier_code = fields.Char(
       'Code',
       related='supplier_id.ref',

   )

    is_shipment = fields.Boolean(
        'Shipment',
    )




 #
 #    self.add_follower(employee_id)
 # self.add_follower(cr, uid, [hr_holiday_id], employee_id, context=context)


from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import SUPERUSER_ID




class SaleOrderOsv(osv.osv):
    _inherit = "sale.order"

    def create(self, cr, uid, vals, context=None):
        if 'is_mto' in vals:
            if vals['is_mto']:
                user = self.pool.get('res.users').browse(cr, uid, context=context)
                # Supplier creates MTO: it must be is_shipment (this field will also be invisible for supplier)
                if user.has_group('model_security_adjust_oaw.group_supplier'):
                    vals['is_shipment'] = True
                    print "Suppliers mto and shipment"
                # Internal MTO: supplier_id must be selected
                if not user.has_group('model_security_adjust_oaw.group_supplier'):
                    if 'supplier_id' in vals:
                        if not vals['supplier_id']:
                            raise osv.except_osv(_('Error!'), _('For MTO, you must select "Sales Supplier"'))


        res = super(SaleOrderOsv, self).create(cr, uid, vals, context=context)
        rec = self.browse(cr, uid, res, context=context)
        if rec.supplier_id:
            self.message_subscribe(cr, SUPERUSER_ID, [rec.id], [rec.supplier_id.id], context=context)
        return res



    def write(self, cr, uid, ids, vals, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.is_mto:
                user = self.pool.get('res.users').browse(cr, uid, context=context)
                # Supplier modifies MTO: it must be is_shipment (this field will also be invisible for supplier)
                # This for the case Internal User creates for Supplier shipment-mto (Selecting supplier as sales person)
                if user.has_group('model_security_adjust_oaw.group_supplier'):
                    vals['is_shipment'] = True
                    print "Suppliers mto and shipment"
                # Internal MTO: supplier_id must be selected
                if not user.has_group('model_security_adjust_oaw.group_supplier'):
                    if 'supplier_id' in vals:
                        if not vals['supplier_id']:
                            raise osv.except_osv(_('Error!'), _('For MTO, you must select "Sales Supplier"'))
        res = super(SaleOrderOsv, self).write(cr, uid, ids, vals, context=context)
        for rec in self.browse(cr, uid, ids, context=context):
            if rec.supplier_id:
                self.message_subscribe(cr, SUPERUSER_ID, [rec.id], [rec.supplier_id.id], context=context)
        return res
