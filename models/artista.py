# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Artista(models.Model):
    # Hace falta poner fest.artista??, porque como he llamado al modelo ofm pero en el pdf pone fest, creo que no pasa na
    _inherit = "ofm.participante"
    _name = "ofm.artista"
    _description = "Artista del Festival"
    # ¿Hace falta? _rec_name='nombre', en el padre si esta puesto

    # Genero Musical del Artista
    genero_musical = fields.Char(
        string="Genero Musical", required=True, help="Genero Musical", size=50
    )
    # Caché del Artista
    cache = fields.Float(string="Caché", help="Caché del artista en euros")
    # Rider Técnico del Artista
    rider_tecnico = fields.Text(string="Rider Tecnico")

    # Validación del caché del artista, debe ser inferior a 3.000€
    @api.constrains("cache")
    def _check_cache(self):
        if self.cache >= 3000:
            raise models.ValidationError(
                "El caché del artista debe ser inferior a 3.000€."
            )

    # Restricción SQL para que el salario no sea negativo
    _sql_constraints = [
        (
            "salario_positivo_check",
            "CHECK(salario >= 0)",
            "El salario no puede ser negativo.",
        )
]
