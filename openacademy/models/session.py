from odoo import models, fields, api


class session(models.Model):
    _name = 'openacademy.session'
    _description = 'Openacademy sessions'

    name = fields.Char(required=True, index=True, string="Nom")
    start_date = fields.Date(string='Start date', default=fields.Date.today())
    duration = fields.Float(digits=(6, 2))
    seats = fields.Integer(string="Number of seats")
    course_id = fields.Many2one('openacademy.cours', string="Course", ondelete='cascade', index=True)
    attendees_ids = fields.Many2many("res.partner", string="Attendees")
    percentage = fields.Float(compute="_compute_percentage")

    @api.depends('seats', 'attendees_ids')
    def _compute_percentage(self):
        for record in self:
            if not record.seats:
                record.percentage = 0
            else:
                record.percentage = len(record.attendees_ids) * 100 / record.seats
        return record.percentage

    @api.onchange('seats', 'attendees.ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Invalid number of seats value",
                    'message': "Number of seats can not be negative"
                },
            }
        if self.seats < len(self.attendees_ids):
            return {
                'warning': {
                            'title': "Too many attendees!",
                            'message': "Send some attendees home"
                            },
            }
