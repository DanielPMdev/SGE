# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Song(models.Model):
    _name = 'music_management.song'
    _description = 'Canciones creadas por Artistas pertenecientes a Albums'

    #Atributos
    name = fields.Char(string='Nombre de la Canción', required=True)
    genre = fields.Char()
    
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
    #Relaciones 
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
