from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.university_teacher.report_class_detail.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            row = 3
            col = 3
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.set_column('D:E', 25)
            sheet.write(row, col, obj.name, bold)
            sheet.write(row + 2, col, 'Students', bold)
            row += 3
            for student in obj.students:
                row += 1
                sheet.write(row, col, student.name, bold)
                sheet.write(row, col + 1, student.name, bold)
                sheet.write(row, col + 2, student.name, bold)
