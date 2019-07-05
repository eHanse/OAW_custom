
from openerp import models, fields, api

class ResUser(models.Model):
    _inherit = "res.users"

    is_supplier = fields.Boolean(
        related="partner_id.supplier",
        readonly=True,
        store=True,
    )
    is_customer = fields.Boolean(
        related="partner_id.customer",
        readonly=True,
        store=True
    )



# object action for chrono update button in sale order form view
    @api.multi
    def action_orders_3(self):
        view_id = self.env.ref('base.view_users_form').id
        context = {}
        return {
            'name':'External Users',
            'view_mode':'form',
            'view_type': 'form',
            'res_model':'res.users',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'res_id':self.id,
            'context':context,
        }

