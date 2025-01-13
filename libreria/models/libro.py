# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Libros para Librería Bosco'

    name = fields.Char(string="Nombre del Libro", required=True)
    numPaginas = fields.Integer(string="Número de Páginas")
    ISBN = fields.Char()
    ubicacion = fields.Char()
    sinopsis = fields.Text(string="Sinopsis del libro")
    fechaPublicacion = fields.Date(string="Fecha de Publicación")
    es_bestseller = fields.Boolean()
    portada = fields.Image(max_width=100, max_height=130)
    
    
    #RELACIONES
    #Un libro pertenece a un autor y muchos libros pueden ser a un autor
    autor_id = fields.Many2one('libreria.autor', string='Autor')
    
    #Un libro puede tener varios géneros y un género tiene muchos libros
    genero_ids = fields.Many2many('libreria.genero', string='Géneros')
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

