{
    'name': 'View adjustments',
    'version': '0.6',
    'author': 'eHanse',
    'website': 'https://www.ehanse.de',
    'category': 'Not a Partner yet',
    'depends': ["base",
                "sale",
                "account_voucher",
                "sale_line_quant",
                "sale_line_quant_extended",
                "stock",
                "oa_order_line_views"
                ],
    'description': """
* moves and creates, makes tabs invisible, minor adjustments on Customer/Supplier Payments
    """,
    'data': [
        'views/account_voucher_views.xml',
    ],
    'installable': True,
}
