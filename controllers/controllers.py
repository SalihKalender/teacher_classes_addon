# -*- coding: utf-8 -*-
from odoo.http import request, Controller, route


class Homepage(Controller):
    @route('/university_teacher/homepage', auth='public', website=True)
    def main_page(self):
        return request.render('university_teacher.main_page')


class Classes(Controller):
    @route('/university_teacher/classes', auth='user', website=True)
    def get_classes(self):
        classes = request.env['class.room'].search([])
        val = {
            'classes': classes
        }
        return request.render('university_teacher.classes_page', val)

    @route('/university_teacher/add_class', auth='user', website=True, csrf=True)
    def get_university_class_form(self):
        return request.render('university_teacher.add_class')

    @route('/university_teacher/created/class', auth='user', method='POST', website=True)
    def add_university_class(self, **kw):
        print(kw)
        print(kw.get('class_name'))
        val = {
            'name': str(kw.get('class_name'))
        }
        new_class = request.env['class.room'].create(val)
        for key, value in kw.items():
            if key.startswith('student_'):
                val = {
                    'name': value,
                    'class_room': new_class.id
                }
                print(val)
                request.env['student.student'].create(val)
        return self.get_classes()


class Students(Controller):
    @route('/university_teacher/classes/students/<int:student_id>', auth='user', website=True) 
    def get_class_student(self, student_id, **kw):
        selected_student = request.env['student.student'].search([('id', '=', student_id)])
        exams = []
        if selected_student.exams:
            for exam in selected_student.exams:
                exam_name = exam.exam_name.name
                exam_date = exam.exam_date
                exam_point = exam.point
                val = {
                    'name': exam_name,
                    'date': exam_date,
                    'point': exam_point
                }
                print(val)
                exams.append(val)
        val = {
            'student':  selected_student, 'exams': exams
        }
        return request.render('university_teacher.student_detail_page', val)


class Exams(Controller):
    @route('/university_teacher/exams', auth='user', website=True)
    def get_exams(self):
        exams = request.env['class.exam'].search([])
        val = {
            'exams': exams
        }
        return request.render('university_teacher.exam_list', val)

    @route('/university_teacher/add_exam', auth='user', website=True, csrf=True)
    def add_exam(self):
        classes = request.env['class.room'].search([])
        val = {
            'classes': classes
        }
        return request.render('university_teacher.add_exam', val)

    @route('/university_teacher/created/exam', auth='user', method='POST', website=True)
    def create_exam(self, **kw):
        print(kw)
        exam_class_ids = []
        for key, value in kw.items():
            if key.__contains__('class_'):
                exam_class_ids.append(value)
        exam_val = {
            'name': kw.get('exam_name'),
            'date': kw.get('exam_date'),
            'classes': request.env['class.room'].search([('id', 'in', exam_class_ids)])
        }
        exam_record = request.env['class.exam'].create(exam_val)
        for key, value in kw.items():
            if key.startswith('student_'):
                print('student_ %s' % key[8:])
                val = {
                    'exam_name': exam_record.id,
                    'point': value,
                    'student_name': request.env['student.student'].search([('id', '=', int(key[8:]))]), 
                }
                print(val)
                request.env['exam.results'].create(val)
        return self.get_exams() 
