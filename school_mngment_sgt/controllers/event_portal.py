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

class EventPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        event_count = http.request.env['event.event'].sudo().search_count([])
        values['event_count'] = event_count
        return values



    @http.route(['/my/events', '/my/events/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_events(self, **kwargs):
        events = request.env['event.event'].sudo().search([])
        # events = request.env['event.event'].sudo().search([('user_id', '=', request.env.user.id)])
        values = {
            'events': events
        }
        return request.render("school_mngment_sgt.portal_my_events", values)

    @http.route(
        ["/my/event/<int:event_id>"], type="http", auth="public", website=True
    )
    def portal_my_event(self, event_id, access_token=None, **kw):
        event_obj = request.env['event.event'].sudo().browse(event_id)
        return request.render("school_mngment_sgt.portal_my_event",
                              {
                                  "event_obj": event_obj,
                              })

