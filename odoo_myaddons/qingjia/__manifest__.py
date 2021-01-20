# -*- coding: utf-8 -*-
{
    'name': "请假",

    'summary': """
        请假""",

    'description': """
        请假单
    """,
    'sequence':2,

    'author': "FQ",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        #'views/yuangong.xml',
        #'views/workflow.xml',
        'views/user.xml',
        'views/manager.xml',
        'views/Action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_increment': False,
}
