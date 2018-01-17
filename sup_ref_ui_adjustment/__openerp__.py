# -*- coding: utf-8 -*-
{
    'name': "Show Supplier Reference",

    'summary': """
      Views related to Supplier Reference. """,

    'description': """
         Adds partner_ref to tree and search views OPOL, PO, RFQ, On Draft Invoices
    """,

    'author': "OA Watches",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ["base","purchase","sale_line_quant","purchase_view_adjust_oaw",'account'],

    # always loaded
    'data': ["views/purchase_views.xml",
             "views/account_invoice_views.xml",
             ],
    'installable': True,    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}