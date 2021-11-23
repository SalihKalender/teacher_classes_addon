from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.university_teacher.report_student_detail.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Student Details')
        bold = workbook.add_format({'bold': True})
        row = 3
        col = 3
        sheet.set_column('D:E', 14)
        sheet.set_column('F:G', 25)
        for obj in partners:
            sheet.write(row, col, 'Name', bold)   # 3.satir, 3.sutun'dan sonraki satir ve sutunlar, yani 4.satir 4.sutun
            sheet.write(row, col + 1, obj.name, bold)
            sheet.write(row + 1, col, 'Class', bold)
            sheet.write(row + 1, col + 1, obj.class_room.name, bold)
            row += 2
            for exam in obj.exams:
                sheet.write(row, col, exam.exam_date, bold)
                sheet.write(row, col + 1, 'Exam Name', bold)
                sheet.write(row, col + 2, exam.exam_name.name, bold)
                sheet.write(row, col + 3, 'Point', bold)
                sheet.write(row, col + 4, exam.point, bold)
                row += 1
            row += 3
