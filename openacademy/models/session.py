from odoo import models, fields, api


class session(models.Model):
    _name = 'openacademy.session'
    _description = 'Openacademy sessions'

    name = fields.Char(required=True, index=True, string="Nom")
    start_date = fields.Date(string='Start date')
    duration = fields.Float(digits=(6, 2))
    seats = fields.Integer(string="Number of seats")
