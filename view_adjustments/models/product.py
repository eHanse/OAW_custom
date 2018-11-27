'''
Created on 27 Apr, 2015

@author: roomsfor
'''
from openerp.tools.translate import _
from openerp import models, fields, api, _
from openerp.osv import fields, osv


class product_template(osv.osv):
    _inherit = 'product.template'
    _name = 'product.template'
    _columns = {
                'additional_info': fields.text('additional_info')
                }
        
     
# This line adds to the product relation the field "Additional Info" and assigns its value to the xml-field "additional_info" 
    

# vim:expandtab:smartinddent:tabstop=4:softtabstop=4:shiftwidth=4: