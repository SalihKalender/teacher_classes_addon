# -*- coding: utf-8 -*-
{
    'name': "university_teacher",

    'summary': """
        Bir Uni ogretmeninin siniflari ve ogrencilerinin kaydini ve onlarin sinav bilgilerini tutacal bir module
    """,

    'description': """
        Uni Sınıflar,
        Uni Ogrenciler,
        Uni sinavlar
    """,

    'author': "Salih Kalender",
    'website': "https://github.com/SalihKalender",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'website',
        'web',
        'mail',
        'report_xlsx'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/list_files.xml',
        'wizard/create_exam_report_view.xml',
        'wizard/menu.xml',
        'views/class_view.xml',
        'views/exam_view.xml',
        'views/student_view.xml',
        'views/menu.xml',
        'views/homepage_template_view.xml',
        'views/classes_template_view.xml',
        'views/student_detail_template_view.xml',
        'views/exam_list_template_view.xml',
        'views/add_exam_template_view.xml',
        'views/add_class_template_view.xml',
        'views/menu_template_view.xml',
        'report/student_detail.xml',
        'report/class_room_detail.xml',
        'report/exam_detail.xml',
        'report/wizard_exam_detail.xml',
        'report/report.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': -150,
    'installable': True,
    'application': True,
    'auto_install': False,
}
