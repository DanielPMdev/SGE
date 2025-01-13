# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Genero(models.Model):
    _name = 'libreria.genero'
    _description = 'Género Literario'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripcion")
    
    
    #RELACIONES
    #Un genero puede pertenecer a muchos libros y un libro puede tener varios generos
    libro_ids = fields.Many2many('libreria.libro', string='Libros')
    
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100