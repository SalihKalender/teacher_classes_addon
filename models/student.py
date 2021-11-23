from odoo import models, fields, api


class Student(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'student.student'
    _description = 'University Teacher Students'

    name = fields.Char(string='Student Name', required=True)
    class_room = fields.Many2one('class.room', string='Sinif', ondelete='cascade', required=True)  # yani ilgili class silindiginde bu ogrencilerde silinecek
    exams = fields.Many2many('exam.results', 'student_exam_rel', 'exam_id', 'student_id', string='Exam Name')   # tracking=True yaparsan degisim falan oldugunda altta oe_chatter'a yazar
    _rec_name = 'name'
    _order = 'class_room asc, name asc'

    def unlink(self):
        print('AAA')
        return super(Student, self).unlink()
