# -*- coding: utf-8 -*-
from odoo import http

# class Qingjia111(http.Controller):
#     @http.route('/qingjia111/qingjia111/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qingjia111/qingjia111/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qingjia111.listing', {
#             'root': '/qingjia111/qingjia111',
#             'objects': http.request.env['qingjia111.qingjia111'].search([]),
#         })

#     @http.route('/qingjia111/qingjia111/objects/<model("qingjia111.qingjia111"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qingjia111.object', {
#             'object': obj
#         })