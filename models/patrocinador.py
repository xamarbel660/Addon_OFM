from odoo import models, fields, api

class Patrocinador(models.Model):
    _name = "ofm.patrocinador"
    _description = "patrocinador de la fiesta"
    
    name = fields.Char(
        string='Nombre del patrocinador',
        required=True
    )

    pais = fields.Many2one("res.country", "Pais")

    escenarios_ids = fields.Many2many(
        comodel_name="ofm.escenario",
        inverse_name="patrocinadores_ids",
        string="Escenarios"
    )
    
    numero_de_escenarios = fields.Integer(string="Cantidad de escenarios patrocinados", compute="_compute_cant_escenarios", store=True)

    @api.depends('escenarios_ids')
    def _compute_cant_escenarios(self):
        for record in self:
            record.numero_de_escenarios = len(record.escenarios_ids)