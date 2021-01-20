# -*- coding: utf-8 -*-
{
    'name': "考勤表",

    'summary': """
        employee""",

    'description': """
        考勤表
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence':0,

    # any module necessary for this one to work correctly
    'depends': ['base','hr','qingjia'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
        'views/action.xml',
        'views/kanban.xml',
        'views/calendar.xml',
        'views/report.xml',
        'report/sql_view.xml',
        'report/sql_report_pdf.xml',
        'wizard/wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_increment': False,
}