# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def _update_prod_tmpl_fields(cr, registry):

    # updates total field, that keeps total sale amount for each product.
    sql = '''
    UPDATE
        product_template pt
    SET
        total = subquery.amount
    FROM (
        SELECT
            pt.id AS pt_id,
            SUM(pt.total) AS amount
        FROM
            sale.order.line sol
            JOIN product_template  pt ON sol.product_tmpl_id = pt_id
        WHERE
            sol.state = 'sent'
        ) AS subquery
    WHERE pt.id = subquery.pt_id
    '''

    cr.execute(sql)

