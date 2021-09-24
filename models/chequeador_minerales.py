from odoo import fields, models

class Minerlales(models.Model):

    _name           = "chequeador.minerales"
    _description    = "Gestionar diferentes minrales minados"

    name            = fields.Char(required = True, string="Mineral")