# -*- coding: utf-8 -*-


def _update_description_field(cr, registry):
    # updates new_description field in purchase_order_line
    cr.execute('''
           UPDATE
           purchase_order_line pol
           SET
           default_code = subquery.default_code
           FROM (
               SELECT
               pp.default_code AS default_code,
               pp.id AS prod_id
               FROM
               product_product pp
               ) AS subquery
           WHERE subquery.prod_id = pol.product_id
       ''')
    # updates new_description field in stock move
    cr.execute('''
    UPDATE
        stock_move sm
    SET
        default_code= subquery.default_code
        FROM (
          SELECT pp.id AS product_id, pp.default_code AS default_code
          FROM product_product pp
          ) AS subquery
    WHERE sm.product_id = subquery.product_id
    ''')
    # updates new_description field in account_invoice_line
    cr.execute('''

   ''')

    # updated new_description field in quants tree view
    cr.execute('''UPDATE
       account_invoice_line ail
       SET
       default_code= subquery.default_code
          FROM (
          SELECT pp.id AS product_id, pp.default_code AS default_code
          FROM product_product pp
         ) AS subquery
       WHERE ail.product_id = subquery.product_id

       ''')
    cr.execute('''
         UPDATE
             stock_quant sq
         SET
         default_code= subquery.default_code
              FROM (
              SELECT pp.id AS product_id, pp.default_code AS default_code
              FROM product_product pp
         ) AS subquery
         WHERE sq.product_id = subquery.product_id
     ''')
    # new_description field in transfer views
    cr.execute('''
        UPDATE
            stock_transfer_details_items items
        SET
            default_code= subquery.default_code
            FROM (
              SELECT pp.id AS product_id, pp.default_code AS default_code
              FROM product_product pp
         ) AS subquery
        WHERE items.product_id = subquery.product_id
    ''')
