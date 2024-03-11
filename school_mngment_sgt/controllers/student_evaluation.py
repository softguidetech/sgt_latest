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

class EvalPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        # eval_count = http.request.env['school.evaluation'].sudo().search_count([])
        eval_count = http.request.env['school.evaluation'].sudo().search_count([('student_id.partner_id', '=', request.env.user.partner_id.id),('type','=','student')])
        values['eval_count'] = eval_count
        return values

    @http.route(['/my/evaluations', '/my/evaluations/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_evaluations(self, **kwargs):
        evaluations = request.env['school.evaluation'].sudo().search([('student_id.partner_id', '=', request.env.user.partner_id.id),('type','=','student')])
        values = {
            'evaluations': evaluations
        }
        return request.render("school_mngment_sgt.portal_my_evaluations", values)

    @http.route(
        ["/my/evaluation/<int:evaluation_id>"], type="http", auth="public", website=True
    )
    def portal_my_evaluation(self, evaluation_id, access_token=None, **kw):
        evaluation_obj = request.env['school.evaluation'].sudo().browse(evaluation_id)
        return request.render("school_mngment_sgt.portal_my_evaluation",
                              {
                                  "evaluation_obj": evaluation_obj,
                              })

