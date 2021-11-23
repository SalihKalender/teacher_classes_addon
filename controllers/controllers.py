# -*- coding: utf-8 -*-
# from odoo import http


# class UniversityTeacher(http.Controller):
#     @http.route('/university_teacher/university_teacher/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/university_teacher/university_teacher/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('university_teacher.listing', {
#             'root': '/university_teacher/university_teacher',
#             'objects': http.request.env['university_teacher.university_teacher'].search([]),
#         })

#     @http.route('/university_teacher/university_teacher/objects/<model("university_teacher.university_teacher"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('university_teacher.object', {
#             'object': obj
#         })
