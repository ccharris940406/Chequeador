from operator import mod
from odoo import fields, models

class CamionModelo(models.Model):

    _inherit        = ['fleet.vehicle.model']
    _description    = "Definir los modelos de los diferentes camiones"

    capacidad       = fields.Float(string="Capacidad de carga")