# -*- coding: utf-8 -*-
{
    'name': "Gestión Musical by danielpm.dev",

    'summary': "Gestión de música con relaciones y funcionalidades avanzadas",

    'description': """
        Este módulo permite gestionar bandas musicales, sus álbumes y canciones,
        así como crear listas de reproducción personalizadas.
        Incluye funcionalidades avanzadas como cálculos automáticos, 
        formatos personalizados de duración y relaciones entre modelos, 
        brindando una solución completa para la administración de música en Odoo.
    """,

    'author': "Daniel Porras Morales",
    'website': "https://www.linkedin.com/in/danielpmdev/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

