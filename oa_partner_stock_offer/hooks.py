# -*- coding: utf-8 -*-
def _update_partner_offer_fields(cr, registry):

    cr.execute('''
       UPDATE
           supplier_stock
       SET partner_qty = CASE
                WHEN quantity = 0.0 THEN '0'
                WHEN quantity = 1.0 THEN '1'
                WHEN quantity = 2.0  THEN '2'
                WHEN quantity >= 3.0 THEN '>=3'
            END
   ''')

    cr.execute('''
        UPDATE
            supplier_stock ss
        SET
            lowest_cost = TRUE
            FROM (
              SELECT
                product_id,
                MIN(price_unit_base) AS min_price
              FROM
                supplier_stock
              GROUP BY
                product_id
            ) AS lowest_price_product
        WHERE
          ss.product_id = lowest_price_product.product_id AND
          ss.product_id = lowest_price_product.min_price
    ''')

