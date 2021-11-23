from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.university_teacher.report_exam_detail.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            row = 3
            col = 3
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.set_column('D:E', 30)
            sheet.set_column('E:F', 30)
            sheet.write(row, col, 'Exam Name', bold)
            sheet.write(row, col + 1, obj.name, bold)
            sheet.write(row, col + 2, 'Date', bold)
            sheet.write(row, col + 3, obj.date, bold)
            sheet.write(row + 1, col, 'RESULTS', bold)
            row += 3
            sheet.write(row, col, 'Students', bold)
            for result in obj.results:
                row += 1
                sheet.write(row, col, 'Student Name', bold)
                sheet.write(row, col + 1, result.student_name.name, bold)
                sheet.write(row, col + 2, 'Class', bold)
                sheet.write(row, col + 3, result.class_room, bold)
                sheet.write(row, col + 4, 'Point', bold)
                sheet.write(row, col + 5, result.point, bold)
