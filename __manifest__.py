# -*- coding: utf-8 -*-
{
    'name': "Invoice Filter and EMS Payment Link",

    'summary': """
        Filter and show self invoice for portal user. EMS students will get invoice link under fees receipt page.
        """,

    'description': """
        Filter and show self invoice for portal user. 
        EMS students will get invoice link under fees receipt page.
    """,

    'author': "Md. Kamrul Hasan",
    'website': "https://daffodil-bd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'school_fees', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/onecard_invoice_link.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
