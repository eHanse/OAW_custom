# -*- coding: utf-8 -*-
{
    'name': "./chr123_reports",

    'summary': """
        Chr123 specific reports""",

    'description': """
        Creates quotation, invoice, move reports for 
        - Chrono123 
        - Timeware 
        - Sino 
        Adds report relevant fields and logic: 
        - partner note 
        - Code (Quoation name and Customer Name
    
        
    """,

    'author': "Chrono123",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Reports',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/quotation_report.xml',
        'views/quotation_report_timeware.xml',
        'views/sale_order_form.xml',
        'views/quotation_report_sino.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
