# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ProductsSalesInit(models.TransientModel):
    _name = "products.sales.wizard"
    _description = 'Products Sales Initialization Wizard '

    @api.multi
    def action_products_sales_initialise(self):
        self.ensure_one()
        if self.env.context.get('active_ids', False):
            pts = self.env.context.get('active_ids')
            self.env['product.template']._initialize_values(pts)
        return {'type': 'ir.actions.act_window_close'}
