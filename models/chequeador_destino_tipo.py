from odoo import fields, models

class DestinoTipo(models.Model):

    _name           = "chequeador.destino.tipo"
    _description    = "Para gestionar el tipo de destino hacia donde se realiza la descarga"

    name            = fields.Char(required=True, string="Tipo de destino")
