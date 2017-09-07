{
    'name': "report_custom",
    'sequence': 1,
    'summary': """Customize Pdf Invoice""",

    'description': """
        Development with Odoo
    """,

    'author': "franckysolo",
    'website': "http://www.franckysolo-productions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Reports',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/custom_paperformat.xml',
        'views/report_custom_action.xml',
        'views/report_custom_views.xml',
        'views/custom_cgv.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-



