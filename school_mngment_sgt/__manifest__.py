# -*- coding: utf-8 -*-


{
    'name': 'School Management SGT',
    'version': '17.0.1.0.0',
    'category': 'School Management',
    'summary': 'A Module For School Management',
    'author': "SGT",
     'price': 65,
    'currency': "EUR",
    'website': "http://www.softguidetech.com",
    "depends": ["mail", "hr","stock", "purchase", "account", "fleet", "event", "rating", "crm", "delivery"],
    'data': [
        "security/school_security.xml",
        "security/library_security.xml",
        "security/transport_security.xml",
        "security/assignment_security.xml",
        "security/security_fees.xml",
        "security/timetable_security.xml",
        "security/event_security.xml",
        "security/evaluation_security.xml",
        "security/attendance_security.xml",
        "security/ir.model.access.csv",
        "data/student_sequence.xml",
        "data/mail_template.xml",
        "data/library_sequence.xml",
        "data/library_category_data.xml",
        "data/library_card_schedular.xml",
        "data/transport_schedular.xml",
        "data/school_fees_sequence.xml",
        "data/data.xml",
        "data/exam_sequence.xml",
        "wizard/terminate_reason_view.xml",
        "wizard/reason_wiz_view.xml",
        "views/student_view.xml",
        "views/school_view.xml",
        "views/teacher_view.xml",
        "views/parent_view.xml",
        'views/card_details.xml',
        "views/library_view.xml",
        "views/transport_view.xml",
        "views/homework_view.xml",
        "views/assignment_portal_template.xml",
        "views/account_move.xml",
        "views/school_fees_view.xml",
        "views/payslip_portal_template.xml",
        "views/timetable_view.xml",
        "views/regular_timetable_portal_template.xml",
        "views/exam_timetable_portal_template.xml",
        "views/event_view.xml",
        "views/event_portal_template.xml",
        "views/school_evaluation_view.xml",
        "views/result_portal_template.xml",
        "views/school_attendance_view.xml",
        "views/month_attendance.xml",
        "views/exam_view.xml",
        "wizard/assign_roll_no_wizard.xml",
        "wizard/move_standards_view.xml",
        "wizard/terminate_reason.xml",
        "wizard/terminate_reason.xml",
        "wizard/transfer_vehicle.xml",
        "wizard/transport_terminate_reason_view.xml",
        "wizard/attendance_sheet_wizard_view.xml",
        "wizard/student_attendance_by_month_view.xml",
        "wizard/monthly_attendance_wizard_view.xml",
        "report/report_view.xml",
        "report/identity_card.xml",
        "report/teacher_identity_card.xml",
        "report/qrcode_label.xml",
        "report/participants.xml",
        "report/student_payslip.xml",
        "report/student_fees_register.xml",
        "report/timetable.xml",
        "report/monthly_attendance_report_view.xml",
        "report/additional_exam_report.xml",
        "report/result_information_report.xml",
        "report/batch_exam.xml",
        "wizard/batch_result.xml",
        "wizard/exam_subject_result_view.xml",
        "report/exam_result_report.xml",

    ],
    "demo": [
        "demo/school_demo.xml",
        "demo/library_demo.xml",
        "demo/transport_demo.xml",
        "demo/assignment_demo.xml",
        "demo/school_fees_demo.xml",
        "demo/timetable_demo.xml",
        "demo/event_demo.xml",
        "demo/school_evaluation_demo.xml",
        "demo/school_attendance_demo.xml",
        "demo/exam_demo.xml"
    ],
    "assets": {
        "web.assets_backend": ["/school_mngment_sgt/static/src/scss/schoolcss.scss",
                               "/school_mngment_sgt/static/src/css/school_evaluation.css"
                               ]
    },
    "installable": True,
    "application": True,
    "images": ['static/description/icon.gif'],
}
