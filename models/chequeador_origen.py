from odoo.tools.translate import trans_export
from odoo import fields, models

class Origen(models.Model):

    _name           = "chequeador.origen"
    _description    = "Gestionar diferentes origenes de minado"

    name            = fields.Char(required = True, string="Origen Id")
    tiempo_ciclo    = fields.Float(required=True, string="Tiempo de ciclo")
    mineral         = fields.Many2one("chequeador.minerales", string="Mineral")