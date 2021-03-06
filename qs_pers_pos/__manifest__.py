# -*- coding: utf-8 -*-
{
    'name': "qs_pers_pos",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Valisoa RAMILIJAONA",
    'website': "http://www.valisoaramilijaona.mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'pos_discount'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report_pos_inherited.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'qs_pers_pos/static/src/js/lock_price_discount.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'web.assets_qweb': [
        'qs_pers_pos/static/src/xml/**/*',
    ],
}
