# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Band(models.Model):
    _name = 'music_management.band'
    _description = 'Artista o Grupos'

    #Atributos
    name = fields.Char()
    
    #FALTA EL GENERO DE LA BANDA
    
    
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    
    #Relaciones 
    #Una banda tiene muchos albums y un album pertenece a una sola banda
    album_ids = fields.One2many('music_management.album', 'band_id', string='Libros')
    
    
    #Campo Calculado
    
    albumCount = fields.Integer(string="Número de Albums", compute="_compute_album_count",
                               store=False)
    
    @api.depends('album_ids')
    def _compute_album_count(self):
        for band in self:
            band.albumCount = len(band.album_ids)
    
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
