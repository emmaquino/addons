# -*- coding: utf-8 -*-
{
    'name': "Automobile Fleet Management",

    'summary': """
        Manage fleet vehicles and vehicle lending services to users""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Luisbert A.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Mitur/automobile', #Crear la subcategoria es indispensable para instalar el modulo en una instancia nueva de la base de datos.
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/automobile_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/vehicle_view.xml',
        'views/automobile_menu.xml',
        'views/fleet_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "application": True,
}
