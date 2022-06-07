# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cours(models.Model):
    _name = 'openacademy.cours'
    _description = 'Openacademy courses'

    name = fields.Char(required=True, index=True, string ="Nom")
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible", ondelete="cascade")
    session_id = fields.One2many("openacademy.session", "course_id", string="Sessions", ondelete="cascade")
