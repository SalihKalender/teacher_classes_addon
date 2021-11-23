from odoo import api, fields, models
from odoo.exceptions import UserError


class ClassRoom(models.Model):
    _name = 'class.room'
    _description = 'University Teacher Classes'
    name = fields.Char(string='Class Name', required=True)
    students = fields.One2many('student.student', 'class_room')
    first_letter = fields.Char(string='First Letter', compute='get_first_letter', store=True)
    student_count = fields.Integer(string='Student Count', compute='get_student_count', store=True)

    def get_first_letter(self):
        for rec in self:
            rec.first_letter = rec.name[0]

    def get_student_count(self):
        for rec in self:
            rec.student_count = len(rec.students)
