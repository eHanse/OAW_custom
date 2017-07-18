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
            SUM(sol.price_unit *sol.product_uos_qty *sol.discount) AS amount
          FROM
            sale_order_line sol
            JOIN product_product pp ON sol.product_id = pp.id
            JOIN product_template pt ON pp.product_tmpl_id = pt.id

          WHERE
            sol.state = 'done'
          GROUP BY
            pt.id
          ) AS subquery
    WHERE pt.id = subquery.pt_id
    '''

    cr.execute(sql)

