# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cours(models.Model):
    _name = 'openacademy.cours'
    _description = 'Openacademy courses'

    name = fields.Char(required=True, index=True, string ="Nom")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
