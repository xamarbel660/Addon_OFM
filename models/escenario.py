from odoo import models, fields, api


class Escenario(models.Model):
    _name = "ofm.escenario"
    _description = "Escenario del Festival"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre", required=True)
    lugarFisico = fields.Selection(
        [
            ("escenario_principal", "Escenario Principal"),
            ("carpa_dance", "Carpa Dance"),
            ("carpa_rock", "Carpa Rock"),
            ("carpa_pop", "Carpa Pop"),
        ],
        string="Lugar Fisico",
        default="escenario_principal",
    )

    patrocinadores = fields.Many2many("ofm.patrocinador", string="Patrocinadores")
    actuacion_ids = fields.One2many(
        comodel_name="ofm.actuacion", inverse_name="escenario_id", string="Actuaciones"
    )
