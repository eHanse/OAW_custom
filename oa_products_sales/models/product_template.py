from odoo import api, fields, models
import odoo.addons.decimal_precision as dp

class product_template_ext(models.Model):
    _inherit = 'product.template'
    _description = 'Products Sale'

    total = fields.Float(
        string="Total",
        digits=dp.get_precision('Product Price'),
        readonly=True
    )

    average = fields.Float(
        string="Average Price",
        digits=dp.get_precision('Product Price'),
        readonly=True,
        compute='_calc_average'
    )

    counts = fields.Integer(
        "Qty of Sale Order Lines",
        readonlu=True
    )

    @api.multi
    def _calc_average(self):
        for pt in self:
            if pt.counts != 0:
                pt.average = pt.total / pt.counts

    @api.multi
    def _initialize_values(self, pts):
        sol_object = self.env['sale.order.line']
        for pt in pts:
            print(pt)
            domain = [
                ('product_id.product_tmpl_id', '=', pt.id),
                ('state', '=', 'sale'),
                ('qty_delivered', '>', 0),
            ]
            sols = sol_object.search(domain)
            sols_len = len(sols)
            if sols_len != 0:
                pt.total = 0.0
                pt.counts = sols_len
                for sol in sols:
                    date = sol.order_id.date_order
                    rate = 1.0
                    if date and sol.order_id.currency_id != self.env.user.company_id.currency_id:
                        rate = self.env['res.currency.rate'].search([
                            ('currency_id', '=', sol.order_id.currency_id.id),
                            ('name', '<=', date),
                        ], order='name desc', limit=1).rate or 1.0

                    sol.subtotal_hkd = sol.price_subtotal / rate
                    print(sol.subtotal_hkd)
                    # Updating pt's total
                    pt.total += sol.subtotal_hkd

                # Updating pt's average
                pt.average = pt.total / pt.counts
        return

    # Classical implementation of inline-button (not working)
    @api.multi
    def action_view_sales_ext(self):

        act_obj = self.env['ir.actions.act_window']
        mod_obj = self.env['ir.model.data']

        # product_ids = [x.id for x in self.product_variant_ids]

        # action_id = mod_obj.xmlid_to_res_id('oa_products_sales.report_all_channels_sales_action', raise_if_not_found=True)
        action = self.env.ref('oa_products_sales.report_all_channels_sales_action').read()[0]



        # result['domain'] = "[('product_id','in',[" + ','.join(map(str, product_ids)) + "]),('state','=','done')]"
        # result['domain'] = "[('product_id','in', [%s])]" % ','.join(product_ids)
        print(self.product_variant_ids.ids)
        action['domain'] = [('product_id','in', self.product_variant_ids.ids),('state','=','done')]


        print(action)
        return action

    # @api.multi
    # def action_view_sales_ext(self):
    #     view_id = self.env.ref('oa_products_sales.sale_order_line_tree_z2')
    #     search_view_id = self.env.ref('oa_products_sales.sale_order_line_tree_search')
    #     print(search_view_id.id)
    #     product_ids = [str(x.id) for x in self.product_variant_ids]
    #
    #     # print(','.join(product_ids))
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'sale.order.line',
    #         'name' : self.name,
    #         # view type not necessary anymore
    #         'view_mode': 'tree',
    #         'view_id': view_id.id,
    #         'context': {},
    #         'target': 'current',
    #         'domain': "[('product_id','in', [%s])]" % ','.join(product_ids),
    #         'search_view_id': search_view_id.id
    #     }