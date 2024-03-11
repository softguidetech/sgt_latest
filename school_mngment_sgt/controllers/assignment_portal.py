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

class AssignmentPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        assignment_count = http.request.env['school.student.assignment'].sudo().search_count([('student_id.partner_id', '=', request.env.user.partner_id.id)])
        values['assignment_count'] = assignment_count
        return values



    @http.route(['/my/assignments', '/my/assignments/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_assignments(self, **kwargs):
        assignments = request.env['school.student.assignment'].sudo().search([('student_id.user_id', '=', request.env.user.id)])
        values = {
            'assignments': assignments
        }
        return request.render("school_mngment_sgt.portal_my_assignments", values)

    @http.route(
        ["/my/assignment/<int:assignment_id>"], type="http", auth="public", website=True
    )
    def portal_my_assignment(self, assignment_id, access_token=None, **kw):
        assignment_obj = request.env['school.student.assignment'].sudo().browse(assignment_id)
        return request.render("school_mngment_sgt.portal_my_assignment",
                              {
                                  "assignment_obj": assignment_obj,
                              })

