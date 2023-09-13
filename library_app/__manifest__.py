# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Manage library catalog and book lending.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Luisbert A.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Mitur/library', #Crear la subcategoria es indispensable para instalar el modulo en una instancia nueva de la base de datos.
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'data/res.partner.csv',
        'data/library.book.csv',
        'data/book_demo.xml',
    ],

    "application": "True",
}
