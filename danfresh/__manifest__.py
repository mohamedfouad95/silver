# -*- coding: utf-8 -*-
{
    'name': "Danfresh",

    'summary': """
        
        """,

    'description': """
    This Module Feature is:\n
        1-Recurring Expenses.\n
          
    """,

    'author': "Odoo Mates",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'hr',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_expense', 'hr_payroll', 'project', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/expense_template.xml',
        'views/ir_cron.xml',
        'views/project_view.xml',
        'views/employee_view.xml',
        'views/hr_payroll_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
