# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Album(models.Model):
    _name = 'music_management.album'
    _description = 'Album creado por Artistas'

    #Atributos
    name = fields.Char()
    releaseYear = fields.Date(string="Año de Lanzamiento")
    albumCover = fields.Image( string="Portada del Album", max_width=100, max_height=130)
    
    #Relaciones 
    #Un album es de una sola banda y una banda puede tener varios albums
    band_id = fields.Many2one('music_management.band', string='Band')
    
    #Un album puede tener varias canciones y una cancion sera de un solo album
    song_ids = fields.One2many('music_management.song', 'album_id', string='Canciones')
    
    #Campo Calculado
    songCount = fields.Integer(string="Número de Canciones", compute="_compute_song_count",
                                  store=False)
    
    albumDuration = fields.Integer(string="Duración Total del Álbum", compute="_compute_album_duration",
                                   store=False) #VER SI QUIERO QUE SE ALMACENE O NO
    
    albumDurationFormatted = fields.Char(string="Duración", compute="_compute_album_duration",
                                         store=False)
    
    @api.depends('song_ids')
    def _compute_song_count(self):
        for album in self:
            album.songCount = len(album.song_ids)
    
    
    @api.depends('song_ids.duration')
    def _compute_album_duration(self):
        for album in self:
            # Sumar los segundos de todas las canciones
            total_seconds = sum(song.duration for song in album.song_ids)
            album.albumDuration = total_seconds

            # Convertir los segundos a HH:MM:SS o MM:SS
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            if hours > 0:
                album.albumDurationFormatted = f"{hours:02}:{minutes:02}:{seconds:02}"
            else:
                album.albumDurationFormatted = f"{minutes:02}:{seconds:02}"