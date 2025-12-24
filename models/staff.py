# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Staff(models.Model):
    # Hace falta poner fest.staff??
    _inherit='ofm.participante'
    _name = 'ofm.staff'
    _description = 'Personal del Festival'
    # ¿Hace falta? _rec_name='nombre'

    # Rol (Seguridad/Técnico)
    rol = fields.Selection([("seguridad", "Seguridad"),
                                    ("tecnico", "Tecnico"),],
                                    "Rol", required=True)
    
    # Tiene que ser un selectiono un char?
    turno = fields.Char(string="Turno", required=True, help="Turno del Staff")
    # turno = fields.Selection([
    #     ('manana', 'Mañana'),
    #     ('tarde', 'Tarde'),
    #     ('noche', 'Noche')
    # ], string="Turno de Trabajo")
    
    salario = fields.Float(string="Salario", help="Salario del trabajador en euros")
    


