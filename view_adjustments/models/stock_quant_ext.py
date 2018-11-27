
from openerp import models, fields, api, _


class StockQuant(models.Model):
    _inherit = 'stock.quant'
    client_order_ref = fields.Char(
        readonly=True,
        string='Remark Of SO',
        compute = '_get_remark',
        default = '',
        store = True

    )
    #
    @api.multi
    # Here, dependence on the sale_id will trigger also!
    @api.depends('sale_id.client_order_ref')
    def _get_remark(self):
        for q in self:
            if q.sale_id:
                q.client_order_ref = q.sale_id.client_order_ref
