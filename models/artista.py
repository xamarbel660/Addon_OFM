# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Artista(models.Model):
    # Hace falta poner fest.artista??
    _inherit='ofm.participante'
    _name = 'ofm.artista'
    _description = 'Artista del Festival'
    # ¿Hace falta? _rec_name='nombre'

    genero_musical = fields.Char(string="Genero Musical", required=True, help="Genero Musical", size=50)
    cache = fields.Float(string="Caché", help="Caché del artista en euros")
    rider_tecnico = fields.Text(string='Rider Tecnico')
    


