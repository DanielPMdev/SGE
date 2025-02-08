# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Genre(models.Model):
    _name = 'music_management.genre'
    _description = 'Genero de las Bandas'

    #Atributos
    name = fields.Char()
    bandCount = fields.Integer(string="Número de Bandas", compute="_compute_band_count",
                                  store=False)

    # Clasificación de bailabilidad (escala 1-5)
    danceRating = fields.Selection(
        selection=[
            ('1', '🎵 - No bailable'),
            ('2', '🎵🎵 - Poco bailable'),
            ('3', '🎵🎵🎵 - Moderadamente bailable'),
            ('4', '🎵🎵🎵🎵 - Muy bailable'),
            ('5', '🎵🎵🎵🎵🎵 - Extremadamente bailable')
        ],
        string="Ranking de Facilidad para Bailar",
    )

    
    #Relaciones 
    #Un genero puede ser de muchas bandas y una banda tiene solo un genero
    band_ids = fields.One2many('music_management.band', 'genre_id', string='Bandas')


    @api.depends('band_ids')
    def _compute_band_count(self):
        for genre in self:
            genre.bandCount = len(genre.band_ids)