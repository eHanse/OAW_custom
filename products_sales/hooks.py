# -*- coding: utf-8 -*-


def _update_prod_tmpl_fields(cr, registry):

    # updates the new field "total" in product_template. It keeps the total sale amount for each product.
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
            sale_order_line sol JOIN product_template pt ON sol.product_tmpl_id = pt.id
          WHERE
            sol.state = 'sent'
          ) AS subquery
    WHERE pt.id = subquery.pt_id
    '''

    cr.execute(sql)

