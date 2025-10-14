# -*- coding: utf-8 -*-
{
    'name': "rental",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
                                      Long description of module's purpose
                                          """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/groups.xml',

        'security/ir.model.access.csv',
        'security/ir_rule.xml',

        # "security/ir_model_access.xml",

        "data/ir_sequence.xml",

        'views/views.xml',
        'views/templates.xml',
        "views/category.xml",
        "views/product.xml",
        'views/customer.xml',
        "views/rental_order.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
