from odoo import models, fields, api

class Escenario(models.Model):
    _name = "ofm.escenario"
    _description = "Escenario de la fiesta"

    name = fields.Text(
        string='Nombre del escenario',
        required=True, unique=True
    )


    ubicacion = fields.Text(string="Ubicación del escenario")

    tema = fields.Text(string="Tema del escenario")

    actuaciones_ids = fields.One2many(
        comodel_name="ofm.actuacion",
        inverse_name="escenario_id",
        string="Actuaciones"
    )

    patrocinadores_ids= fields.Many2many(
        comodel_name="ofm.patrocinador",
        inverse_name="escenario_id",
        string="Patrocinadores"
    )

    numero_de_actuaciones = fields.Integer(string="Cantidad de actuaciones", compute="_compute_cant_actuaciones", store=True)
    numero_de_patrocinadores = fields.Integer(string="Cantidad de patrocinadores", compute="_compute_cant_patrocinadores", store=True)

    @api.depends('actuaciones_ids')
    def _compute_cant_actuaciones(self):
        for record in self:
            record.numero_de_actuaciones = len(record.actuaciones_ids)

    @api.depends('patrocinadores_ids')
    def _compute_cant_patrocinadores(self):
        for record in self:
            record.numero_de_patrocinadores = len(record.patrocinadores_ids)