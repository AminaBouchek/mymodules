from odoo import models, fields


class departement(models.Model):
    _name = "rh.departement"
    _description ="departements list"

    name = fields.Char(string="Nom du departement", index=True)
    site_dep = fields.Char(string="Site du department")
