# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Participante(models.Model):
    _name = 'ofm.participante'
    _rec_name='nombre'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del participante", size=25)
    nacionalidad = fields.Many2one("res.country", "Nacionalidad")
    dni = fields.Char(string="DNI", required=True, help="DNI del participante", size=9)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    activo = fields.Boolean(string="Activo", default=True, readonly=True)
    foto = fields.Binary(string="Foto")
    
    # Restricción de unicidad en el campo DNI
    _sql_constraints = [
        ('dni_uniq',
        'UNIQUE (dni)',
        'El DNI debe ser único.')
    ]

