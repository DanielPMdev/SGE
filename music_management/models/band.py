# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Band(models.Model):
    _name = 'music_management.band'
    _description = 'Artista o Grupos'

    #Atributos
    name = fields.Char()
    
    #Relaciones 
    #Una banda tiene muchos albums y un album pertenece a una sola banda
    album_ids = fields.One2many('music_management.album', 'band_id', string='Libros')
    
    #Una banda tiene un genero y un genero pertenece a muchas bandas
    genre_id = fields.Many2one('music_management.genre', string='Genero')
    
    #Una banda tiene un país y un pais tiene muchas bandas
    country_id = fields.Many2one('res.country', string="País de Origen")

    #Campo Calculado
    albumCount = fields.Integer(string="Número de Albums", compute="_compute_album_count",
                               store=False)
    
    @api.depends('album_ids')
    def _compute_album_count(self):
        for band in self:
            band.albumCount = len(band.album_ids)