# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Artista(models.Model):
    _inherit = "ofm.participante"
    _name = "ofm.artista"
    _description = "Artista del Festival"

    # Genero Musical del Artista
    genero_musical = fields.Char(
        string="Genero Musical", required=True, help="Genero Musical", size=50
    )
    # Caché del Artista
    cache = fields.Float(string="Caché", help="Caché del artista en euros")
    # Rider Técnico del Artista
    rider_tecnico = fields.Text(string="Rider Tecnico")

    # Actuaciones del Artista
    actuacion_ids = fields.Many2many(
        'ofm.actuacion', 
        string="Actuaciones Previstas"
    )

    # Validación del caché del artista, debe ser inferior a 3.000€
    @api.constrains("cache")
    def _check_cache(self):
        if self.cache >= 3000:
            raise models.ValidationError(
                "El caché del artista debe ser inferior a 3.000€."
            )

    # Restricción SQL para que el cache no sea negativo o 0
    _sql_constraints = [
        (
            "cache_positivo_check",
            "CHECK(cache >= 0)",
            "El cache no puede ser negativo o 0.",
        )
]
