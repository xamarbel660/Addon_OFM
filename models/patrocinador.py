from odoo import models, fields, api


class Patrocinador(models.Model):
    _name = "ofm.patrocinador"
    _description = "Patrocinador del Festival"
    _rec_name = "marca"

    marca = fields.Char(string="Marca", required=True)
    dineroPatrocinado = fields.Float(string="Dinero Patrocinado", required=True)

    escenarios = fields.Many2many('ofm.escenario', string='Escenario')
