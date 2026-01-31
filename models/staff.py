# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Staff(models.Model):
    _inherit = "ofm.participante"
    _name = "ofm.staff"
    _description = "Personal del Festival"

    # Rol (Seguridad/Técnico)
    rol = fields.Selection(
        [
            ("seguridad", "Seguridad"),
            ("tecnico", "Tecnico"),
        ],
        "Rol",
        required=True,
    )

    # Turno
    turno = fields.Selection(
        [("manana", "Mañana"), ("tarde", "Tarde"), ("noche", "Noche")],
        string="Turno",
        required=True,
    )

    # Salario
    salario = fields.Float(string="Salario", help="Salario del trabajador en euros")

    # Estado
    state = fields.Selection(
        [
            ("candidato", "Candidato"),
            ("contratado", "Contratado"),
            ("de_baja", "De Baja"),
        ],
        string="Estado",
        default="candidato",
        required=True,
    )

    # Actualizamos las funciones para usar 'state'
    def btn_contratar(self):
        self.write({"state": "contratado"})
        self.write({"activo": True})

    def btn_dar_baja(self):
        self.write({"state": "de_baja"})
        self.write({"activo": False}) 

    def btn_candidato(self):
        self.write({"state": "candidato"})
        self.write({"activo": False})

    # Botones para cambiar el rol del staff
    def btn_rol_to_seguridad(self):
        self.write({"rol": "seguridad"})

    def btn_rol_to_tecnico(self):
        self.write({"rol": "tecnico"})

    # Onchange para el salario dependiendo del rol
    @api.onchange("rol", "salario")
    def onchange_classes(self):
        resultado = {}
        if self.salario > 1500 and self.rol == "tecnico":
            resultado = {
                "value": {"salario": 1500},
                "warning": {
                    "title": "Valores incorrectos",
                    "message": "Un técnico no puede cobrar más de 1500€.",
                },
            }
            return resultado
        elif self.salario > 2000 and self.rol == "seguridad":
            resultado = {
                "value": {"salario": 2000},
                "warning": {
                    "title": "Valores incorrectos",
                    "message": "Un seguridad no puede cobrar más de 2000€.",
                },
            }
            return resultado


    # Restricción SQL para que el salario no sea negativo o 0
    _sql_constraints = [
        (
            "salario_positivo_check",
            "CHECK(salario >= 0)",
            "El salario no puede ser negativo o 0.",
        )
    ]
