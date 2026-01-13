# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Staff(models.Model):
    _inherit='ofm.participante'
    _name = 'ofm.staff'
    _description = 'Personal del Festival'
    # ¿Hace falta? _rec_name='nombre'

    # Rol (Seguridad/Técnico)
    rol = fields.Selection([("seguridad", "Seguridad"),
                                    ("tecnico", "Tecnico"),],
                                    "Rol", required=True)
    
    # Tiene que ser un selection o un char?
    turno = fields.Char(string="Turno", required=True, help="Turno del Staff")
    # turno = fields.Selection([
    #     ('manana', 'Mañana'),
    #     ('tarde', 'Tarde'),
    #     ('noche', 'Noche')
    # ], string="Turno de Trabajo")
    
    salario = fields.Float(string="Salario", help="Salario del trabajador en euros")
    

    # Botones para cambiar el rol del staff
    def btn_rol_to_seguridad(self):
        self.write({'rol':'seguridad'})

    def btn_rol_to_tecnico(self):
        self.write({'rol':'tecnico'})


    # Onchange para el salario dependiendo del rol
    @api.onchange('rol','salario')
    def onchange_classes(self):
        resultado = {}
        if self.salario > 1500 and self.rol == 'tecnico':
            resultado = {
                    'value': {'salario':1500},
                    'warning': {
                        'title':'Valores incorrectos',
                        'message':'Un técnico no puede cobrar más de 1500€.'
                    }
                }
            return resultado
        elif self.salario > 2000 and self.rol == 'seguridad':
            resultado = {
                    'value': {'salario':2000},
                    'warning': {
                        'title':'Valores incorrectos',
                        'message':'Un seguridad no puede cobrar más de 2000€.'
                    }
                }
            return resultado

