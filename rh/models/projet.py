from odoo import models, fields, api

class projet(models.Model):
    _name = "rh.projet"
    _description ="project list"

    code_proj = fields.Char(string="Code de projet", index=True, required=True)
    name= fields.Char(string="Nom de projet", index=True)

