from odoo import models, fields

class employee(models.Model):
    _name = "rh.employee"
    _description ="employees list"

    name = fields.Char(string="Nom", index=True)
    fonction_emp= fields.Char(string="Fonction")
    salaire_emp = fields.Float(string="Salaire")
    num_dep = fields.Many2one('rh.departement', string="Departement")


