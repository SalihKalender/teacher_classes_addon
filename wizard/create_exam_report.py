from odoo import fields, api, models


class CreateClassReport(models.TransientModel): 
    _name = 'create.exam.report.wizard'
    _description = 'Create class Report'

    date_from = fields.Date(string='Date From', required=True)
    date_to = fields.Date(string='Date To', required=True)

    def action_print_report_exams(self):
        exams = self.env['class.exam'].search([('date', '>=', self.date_from), ('date', '<=', self.date_to)])
        is_there_exam = False
        exam_list = []
        if len(exams) > 0:
            is_there_exam = True
            for exam in exams:
                class_list = []
                result_list = []
                for _class in exam['classes']:
                    val = {
                        'name': _class.name
                    }
                    class_list.append(val)
                for result in exam['results']:
                    val = {
                        'student_name': result.student_name.name,
                        'class_room': result.class_room,
                        'point': result.point
                    }
                    result_list.append(val)
                val = {
                    'name': exam.name,
                    'results': result_list,
                    'date': exam.date,
                    'classes': class_list
                }
                exam_list.append(val)

        data = {
            'exams': exam_list,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'is_there_exam': is_there_exam
        }
        return self.env['exam.report.by.date']._print_report(data)


class ExamReportByDate(models.AbstractModel):
    _name = 'exam.report.by.date'

    def _print_report(self, data):
        return self.env.ref('university_teacher.report_menu_exams_detail').report_action(self, data=data)
