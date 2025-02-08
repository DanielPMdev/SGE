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
    'depends': ['base', 'web'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/genre.xml",
        "views/band.xml",
        "views/album.xml",
        "views/song.xml",
        "views/playlist.xml",
        "views/templates.xml",
        "views/menus.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/genre.xml',
        'demo/band.xml',
        'demo/album.xml',    
        'demo/song.xml',
        #'demo/playlist.xml'
    ],
    #'assets': {
        #'web.assets_backend': [
            #'music_management/static/src/js/year_widget.js',
        #],
    #},
}

