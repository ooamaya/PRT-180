# -*- coding: utf-8 -*-

{
    'name': 'Spotify Integration Contacts',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'summary': 'Modulo para recomendar una cancion por genero del contacto',
    'description': 'Modulo para recomendar una cancion por genero del contacto, odoo14',
    'author': 'Omar Amaya',
    'company': 'Prueba Tecnica',
    'images': ['static/description/banner.png'],
    'depends': ['base'],
    'data': [
        'views/res_partner_inherit.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
