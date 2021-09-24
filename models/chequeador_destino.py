from odoo import fields, models

class Destino(models.Model):

    _name           = "chequeador.destino"
    _description    = "Gestioonar los diferentes destinos de descarga"

    name            = fields.Char(required=True, string="Destino Id")
    tipoDestino     = fields.Many2one("chequeador.destino.tipo", required=True, string="Tipo")