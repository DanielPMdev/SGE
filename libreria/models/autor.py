# -*- coding: utf-8 -*-

from odoo import models, fields, api
    
class Autor(models.Model):
    _name = 'libreria.autor'
    _description = 'Autor de Libros'
    
    nombre = fields.Char(string="Nombre del autor", required=True,
                         help="Introduce el escritor de libros")
    
    
    #RELACIONES
    #Un autor tiene muchos libros y un libro tiene un solo autor
    libro_ids = fields.One2many('libreria.libro', 'autor_id', string='Libros')
    
    #Campo Calculado
    numLibros = fields.Integer(string="Número de Libros", compute="_compute_contar_libros",
                               store=False)
    

    @api.depends('libro_ids')
    def _compute_contar_libros(self):
        for autor in self:
            autor.numLibros = len(autor.libro_ids)
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

