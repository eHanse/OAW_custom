# -*- coding: utf-8 -*-


def _update_description_field(cr, registry):

    # updates new_description field in stock move
    cr.execute('''
    UPDATE
        stock_move sm
    SET
        new_description= subquery.name,
        FROM (
          SELECT
            sm.name AS name,
            sm.pt_id
          FROM
            product_template pt
            JOIN product_product pp ON pt.id = pp.product_tmpl_id
            JOIN stock_move sm ON sm.product_id= pt.id
          ) AS subquery
    WHERE sm.product_id = subquery.pt_id
    ''')
    # updates new_description field in account_invoice_line
    cr.execute('''
   UPDATE
       account_invoice_line ail
   SET
       new_description= subquery.name,
       FROM (
         SELECT
           ail.name AS name,
           ail.pt_id
         FROM
           product_template pt
           JOIN product_product pp ON pt.id = pp.product_tmpl_id
           JOIN account_invoice_line sm ON ail.product_id= pt.id
         ) AS subquery
   WHERE ail.product_id = subquery.pt_id
   ''')
    # updates new_description field in purchase_order_line
    cr.execute('''
      UPDATE
          purchase_order_line pol
      SET
          new_description= subquery.name,
          FROM (
            SELECT
              pol.name AS name,
              pol.pt_id
            FROM
              product_template pt
              JOIN product_product pp ON pt.id = pp.product_tmpl_id
              JOIN purchase_order_line pol ON pol.product_id= pt.id
            ) AS subquery
      WHERE pol.product_id = subquery.pt_id
  ''')
    # updated new_description field in quants tree view
    cr.execute('''
         UPDATE
             stock_quant sq
         SET
             new_description= subquery.name,
             FROM (
               SELECT
                 sq.name AS name,
                 sq.pt_id
               FROM
                 product_template pt
                 JOIN product_product pp ON pt.id = pp.product_tmpl_id
                 JOIN stock_quant sq ON sq.product_id= pt.id
               ) AS subquery
         WHERE sq.product_id = subquery.pt_id
     ''')
    # new_description field in transfer views
    cr.execute('''
            UPDATE
                stock_transfer_details_items items
            SET
                new_description= subquery.name,
                FROM (
                  SELECT
                    sq.name AS name,
                    sq.pt_id
                  FROM
                    product_template pt
                    JOIN product_product pp ON pt.id = pp.product_tmpl_id
                    JOIN stock_transfer_details_items items ON items.product_id= pt.id
                  ) AS subquery
            WHERE items.product_id = subquery.pt_id
        ''')
