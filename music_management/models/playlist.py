# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Playlist(models.Model):
    _name = 'music_management.playlist'
    _description = 'Playlist creada'

    #Atributos
    name = fields.Char(string='Nombre de la Playlist', required=True)
    description = fields.Text(string='Descripción')
    playlistCover = fields.Image(string='Portada de la Playlist', max_width=100, max_height=130)
        
    #Relaciones
    #Una playlist tiene varias canciones y una cancion puede estar en varias playlists
    song_ids = fields.Many2many('music_management.song', string='Canciones')
    
    #Campo Calculados
    #Duración total de la playlist en segundos
    playlistDuration = fields.Integer(string="Duración Total de la Playlist", compute="_compute_playlist_duration",
                                      store=False)
    
    playlistDurationFormatted = fields.Char(string="Duración Formateada", compute="_compute_playlist_duration",
                                         store=False)
    
    songCount = fields.Integer(string="Número de Canciones", compute="_compute_song_count",
                                  store=False)
    
    @api.depends('song_ids')
    def _compute_song_count(self):
        for playlist in self:
            playlist.songCount = len(playlist.song_ids)
    
    @api.depends('song_ids.duration')
    def _compute_playlist_duration(self):
        for playlist in self:
            # Sumar los segundos de todas las canciones en la playlist
            total_seconds = sum(song.duration for song in playlist.song_ids)
            playlist.playlistDuration = total_seconds

            # Convertir los segundos a HH:MM:SS o MM:SS
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            if hours > 0:
                playlist.playlistDurationFormatted = f"{hours:02}:{minutes:02}:{seconds:02}"
            else:
                playlist.playlistDurationFormatted = f"{minutes:02}:{seconds:02}"