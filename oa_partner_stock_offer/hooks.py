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
          ss.price_unit_base = lowest_price_product.min_price


    ''')

    cr.execute('''
        UPDATE supplier_stock
            SET has_duplicates=True
            FROM
                (SELECT count(id) COUNT,product_id
                 FROM supplier_stock
                 GROUP BY product_id) AS have_duplicates
        WHERE supplier_stock.product_id=have_duplicates.product_id AND have_duplicates.COUNT >1
    ''')
    # Duplicates of one owner
    cr.execute('''
    UPDATE
      supplier_stock
    SET
      owners_duplicates = True
    FROM
        (
        SELECT count(id) COUNT, product_id, partner_id
        FROM supplier_stock
        GROUP BY product_id, partner_id
        ) AS have_duplicates
    WHERE
      supplier_stock.product_id = have_duplicates.product_id
      AND supplier_stock.partner_id = have_duplicates.partner_id
      AND have_duplicates.COUNT > 1
    ''')

    cr.execute('''
          UPDATE supplier_stock ss
              SET new_description = subquery.name
              FROM
                  (SELECT
                    pt.name AS name,
                    ss.product_id AS prod_id
                   FROM
                    product_template pt
                    JOIN product_product pp ON pt.id = pp.product_tmpl_id
                    JOIN supplier_stock ss ON ss.product_id = pp.id)
                    AS subquery
          WHERE ss.product_id = subquery.prod_id
      ''')






