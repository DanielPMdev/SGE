# -*- coding: utf-8 -*-

from odoo import models, fields, api



class libreria(models.Model):
    _name = 'libreria.libro'
    _description = 'libreria.libro'

    name = fields.Char(string="Nombre del Libro", required=True)
    numPaginas = fields.Integer(string="Número de Páginas")
    ISBN = fields.Char()
    ubicacion = fields.Char()
    sinopsis = fields.Text(string="Sinopsis del libro")
    fechaPublicacion = fields.Date(string="Fecha de Publicación")
    es_bestseller = fields.Boolean()
    portada = fields.Image(max_width=100, max_height=130)
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

