# -*- coding: utf-8 -*-
{
    'name': "order_line_views",

    'summary': """
      Creates order line views for  Internal and Suppler Access user. """,
      
    'description': """
        Menu Items under Sales/Sales lead to tree views of Order Lines.
        This module considers all Order Lines of a (MTO) Sales Order to be supplied by just one supplier.
        Thus, this module adds a Many2one field between sales.order and res_partner models.
    """,

    'author': "OA Trade",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ["base",
                "product",
                "decimal_precision",
                "sale",
                "sale_line_quant_extended",
                "model_security_adjust_oaw",
    ],

    # always loaded
    'data': [
        'views/sale_view.xml',


    ],
    # only loaded in demonstration mode
    #'post_init_hook': '_update_prod_tmpl_fields',
    'installable': True,
    'demo': [],
}
