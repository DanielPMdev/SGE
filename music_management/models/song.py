# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Song(models.Model):
    _name = 'music_management.song'
    _description = 'Canciones creadas por Artistas pertenecientes a Albums'

    #Atributos
    name = fields.Char(string='Nombre de la Canción', required=True)
    duration = fields.Integer(string="Duración en segundos")
    
    # Rating (1-5 estrellas)
    rating = fields.Selection(
        selection=[
            ('1', '⭐'),
            ('2', '⭐⭐'),
            ('3', '⭐⭐⭐'),
            ('4', '⭐⭐⭐⭐'),
            ('5', '⭐⭐⭐⭐⭐')
        ],
        string="Calificación",
        default='1',
        required=True
    )

    #Relaciones 
    #Una cancion pertenece a un solo album y un album tiene muchas canciones
    album_id = fields.Many2one('music_management.album', string='Album')
    
    #Campo relacional indirecto o calculado para acceder al nombre de la banda desde el álbum.
    band_name = fields.Char(related='album_id.band_id.name', string='Banda', store=False)
    
    #Una cancion puede estar en muchas playlist y una playlist tener muchas canciones
    playlist_ids = fields.Many2many('music_management.playlist', string='Playlist')
    
    #Campo Calculados
    #Duración total de la playlist en segundos
    songDurationFormatted = fields.Char(string="Duración Formateada", compute="_compute_song_duration",
                                         store=False)
    

    @api.depends('duration')
    def _compute_song_duration(self):
        for song in self:        
            # Convertir los segundos a HH:MM:SS o MM:SS
            hours, remainder = divmod(song.duration, 3600)
            minutes, seconds = divmod(remainder, 60)
            if hours > 0:
                song.songDurationFormatted = f"{hours:02}:{minutes:02}:{seconds:02}"
            else:
                song.songDurationFormatted = f"{minutes:02}:{seconds:02}"

