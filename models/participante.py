# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Participante(models.Model):
    _name = 'ofm.participante'
    _rec_name='nombre'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del participante", size=25)
    nacionalidad = fields.Many2one("res.country", "Nacionalidad")
    # nacionalidad = fields.Char(string="Nacionalidad", required=True, help="Nacionalidad del participante")
    dni = fields.Char(string="DNI", required=True, help="DNI del participante", size=9)
    
    # Restricción de unicidad en el campo DNI
    
    _sql_constraints = [
        ('dni_uniq',
        'UNIQUE (dni)',
        'El DNI debe ser único.')
    ]

