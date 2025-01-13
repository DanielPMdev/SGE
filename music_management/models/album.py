# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Album(models.Model):
    _name = 'music_management.album'
    _description = 'Album creado por Artistas'

    #Atributos
    name = fields.Char()
    
    #BANDA
    
    relaseYear = fields.Integer()
    albumCover = fields.Image(max_width=100, max_height=130)
    
    #CANTIDAD DE CANCIONES
    
    #DURACION DEL ALBUM
    
    
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()
    
    #Relaciones 
    
    
    #Campo Calculado
    
    
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
