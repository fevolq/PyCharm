# -*- coding: utf-8 -*-
from odoo import http

# class CpoAttendance(http.Controller):
#     @http.route('/cpo_attendance/cpo_attendance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cpo_attendance/cpo_attendance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cpo_attendance.listing', {
#             'root': '/cpo_attendance/cpo_attendance',
#             'objects': http.request.env['cpo_attendance.cpo_attendance'].search([]),
#         })

#     @http.route('/cpo_attendance/cpo_attendance/objects/<model("cpo_attendance.cpo_attendance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cpo_attendance.object', {
#             'object': obj
#         })