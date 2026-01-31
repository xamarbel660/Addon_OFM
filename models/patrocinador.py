from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Patrocinador(models.Model):
    _name = "ofm.patrocinador"
    _description = "patrocinador de la fiesta"
    
    name = fields.Char(
        string='Nombre del patrocinador',
        required=True
    )

    pais = fields.Many2one("res.country", "Pais")

    state= fields.Selection(
        selection=[('propuesto', 'Propuesto'), ('activo', 'Activo'), ('cancelado', 'Cancelado')],
        default='propuesto',
        required=True
    )

    escenarios_ids = fields.Many2many(
    comodel_name="ofm.escenario",
    string="Escenarios"
)
    
    numero_de_escenarios = fields.Integer(string="Cantidad de escenarios patrocinados", compute="_compute_cant_escenarios", store=True)

    @api.depends('escenarios_ids')
    def _compute_cant_escenarios(self):
        for record in self:
            record.numero_de_escenarios = len(record.escenarios_ids)
    

    def action_patrocinador_activo(self):
        self.write({'state': 'activo'})

    def action_patrocinador_cancelado(self):
        self.write({'state': 'cancelado'})

    def action_patrocinador_propuesto(self):
        self.write({'state': 'propuesto'})

    @api.constrains('escenarios_ids')
    def _check_escenarios_activos(self):
        for record in self:
            if record.escenarios_ids and record.state != 'activo':
                raise ValidationError(
                    f"El patrocinador {record.name} debe estar activo para tener escenarios patrocinados."
                )