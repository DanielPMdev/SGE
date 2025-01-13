# -*- coding: utf-8 -*-
{
    'name': "Gestión de Librería DanielPM",

    'summary': "Aplicación de Gestión de una Libreía",

    'description': """
    Aplicación de gestión de librería para el IES Juan Bosco de Alcázar de San Juan, creado en la asignatura de SGE para
    practicar el desarrollo de módulos de odoo con python
    """,

    'author': "Daniel Porras Morales",
    'website': "https://www.linkedin.com/in/danielpmdev/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/libro.xml',
        'views/autor.xml',
        'views/genero.xml',
        'views/menus.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

