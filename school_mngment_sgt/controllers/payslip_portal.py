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

class PayslipPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        # payslip_count = http.request.env['student.payslip'].sudo().search_count([])
        payslip_count = http.request.env['student.payslip'].sudo().search_count([('student_id.partner_id', '=', request.env.user.partner_id.id)])
        values['payslip_count'] = payslip_count
        return values

    @http.route(['/my/payslips', '/my/payslips/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_payslips(self, **kwargs):
        payslips = request.env['student.payslip'].sudo().search([('student_id.partner_id', '=', request.env.user.partner_id.id)])
        # payslips = request.env['student.payslip'].sudo().search([])
        values = {
            'payslips': payslips
        }
        return request.render("school_mngment_sgt.portal_my_payslips", values)

    @http.route(
        ["/my/payslip/<int:payslip_id>"], type="http", auth="public", website=True
    )
    def portal_my_payslip(self, payslip_id, access_token=None, **kw):
        payslip_obj = request.env['student.payslip'].sudo().browse(payslip_id)
        return request.render("school_mngment_sgt.portal_my_payslip",
                              {
                                  "payslip_obj": payslip_obj,
                              })

