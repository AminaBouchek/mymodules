from odoo import models, fields, api

class travail(models.Model):
    _name = "rh.travail"
    _description ="travaux list"

    num_employee = fields.Many2many('rh.employee', string="Employees", ondelete='cascade', index=True)
    code_proj = fields.Many2one('rh.projet', string="Projet", ondelete='cascade', index=True)


