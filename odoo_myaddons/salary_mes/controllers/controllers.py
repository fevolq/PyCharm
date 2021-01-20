# -*- coding: utf-8 -*-
from odoo import http

# class SalaryMes(http.Controller):
#     @http.route('/salary_mes/salary_mes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salary_mes/salary_mes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('salary_mes.listing', {
#             'root': '/salary_mes/salary_mes',
#             'objects': http.request.env['salary_mes.salary_mes'].search([]),
#         })

#     @http.route('/salary_mes/salary_mes/objects/<model("salary_mes.salary_mes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salary_mes.object', {
#             'object': obj
#         })