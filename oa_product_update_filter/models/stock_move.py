from openerp import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'



    # For VCI Currency Amount Price Change Filter
    @api.multi
    def write(self, vals):
        # Check if the stock.move is being confirmed
        if 'state' in vals and vals['state'] == 'done':
                # Loop through the Moved Quants of the stock.move
                for stock_move in self:
                    # Check whether it is a VCI stock move
                    if stock_move.partner_id != 1 and stock_move.quant_owner_id != 1:
                        # Look through existing quants of given produdct_id
                        domain = [
                            ('product_id', '=', stock_move.product_id.id),
                            ('owner_id', '!=', 1),
                            ('location_id', '=', 12),
                        ]
                        stock_quants = self.env['stock.quant'].search(domain, order='create_date DESC')
                        if stock_quants:
                            print quant.purchase_price_unit
                            if stock_quants.purchase_price_unit != stock_move.purchase_price_unit:
                                stock_move.product_id.product_tmpl_id.currency_price_change_date = fields.Datetime.now()
        res = super(StockMove, self).write(vals)
        return res