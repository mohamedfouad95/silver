# -*- coding: utf-8 -*-
{
    'name': "silver_project",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','project','note'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/project_view.xml',
        'security/ir_rule.xml',
        'views/note_views.xml'
    ],

}