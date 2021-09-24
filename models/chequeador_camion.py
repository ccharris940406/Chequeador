from odoo import fields, models

class Camion(models.Model):
    _inherit        =   ['fleet.vehicle']
    _description    =   "Gestionar camiones"

    radio_number    =   fields.Char(string="Radio No.")