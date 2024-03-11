from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request
import werkzeug
from odoo.osv.expression import AND, OR
from odoo.tools import groupby as groupbyelem
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from collections import OrderedDict
from operator import itemgetter
from odoo.exceptions import AccessError, MissingError
import base64
from odoo.tools import plaintext2html
from datetime import datetime, timedelta,date

class ExamTimetablePortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        exam_timetable_count = http.request.env['time.table'].sudo().search_count([('timetable_type','=','exam')])
        values['exam_timetable_count'] = exam_timetable_count
        return values



    @http.route(['/my/exam/timetables', '/my/exam/timetables/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_exam_timetables(self, **kwargs):
        exam_timetables = request.env['time.table'].sudo().search([('timetable_type','=','exam')])
        values = {
            'exam_timetables': exam_timetables
        }
        return request.render("school_mngment_sgt.portal_my_exam_timetables", values)

    @http.route(
        ["/my/exam/timetable/<int:exam_timetable_id>"], type="http", auth="public", website=True
    )
    def portal_my_exam_timetable(self, exam_timetable_id, access_token=None, **kw):
        exam_timetable_obj = request.env['time.table'].sudo().browse(exam_timetable_id)
        return request.render("school_mngment_sgt.portal_my_exam_timetable",
                              {
                                  "exam_timetable_obj": exam_timetable_obj,
                              })

