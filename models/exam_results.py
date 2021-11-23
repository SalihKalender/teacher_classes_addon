from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class ExamResults(models.Model):
    _name = 'exam.results'

    exam_name = fields.Many2one('class.exam', ondelete='cascade')
    student_name = fields.Many2many('student.student', 'student_exam_rel', 'student_id', 'exam_id', string='Student Name')
    # student_name = fields.Many2one('student.student', string='Student Name')
    point = fields.Integer(string='Point')
    display_name = fields.Char(string='Student Name', compute='get_student_name', store=False)
    exam_date = fields.Char(string='', compute='compute_exam_date', store=False)
    class_room = fields.Char(string='Class Room', compute='compute_student_class')

    def get_student_name(self):
        for rec in self:
            rec.display_name = rec.student_name.name

    def compute_exam_date(self):
        for rec in self:
            rec.exam_date = rec.exam_name.date

    def create(self, vals_list):
        print(self.student_name)
        return super(ExamResults, self).create(vals_list)

    def compute_student_class(self):
        for rec in self:
            rec.class_room = rec.student_name.class_room.name


