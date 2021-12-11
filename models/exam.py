from odoo import fields, api, models


class Exam(models.Model):
    _name = 'class.exam'
    name = fields.Char('Exam Name', required=True)
    classes = fields.Many2many('class.room', string='Classes', required=True)
    date = fields.Date('Sinav Tarihi', required=True)
    results = fields.One2many('exam.results', 'exam_name')

    @api.onchange('classes')
    def get_students_on_tree(self):
        self.results = None     
        for rec in self:
            student_lines = []
            for line in self.classes.students:
                names = {
                    'student_name': line
                }
                student_lines.append((0, 0, names))
            rec.results = student_lines

