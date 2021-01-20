# -*- coding: utf-8 -*-
from odoo import models,fields,api,tools

class SQLReport(models.Model):
    _name = 'cpo.attendance_sql'
    _auto = False

    # cpo_id = fields.Char(string='员工ID')
    cpo_name = fields.Char(u'员工姓名')
    cpo_late = fields.Char(u'迟到')
    cpo_early = fields.Char(u'早退')
    cpo_absence = fields.Char(u'缺勤')
    cpo_leave = fields.Char(u'请假')
    cpo_times = fields.Char(u"总工时（小时）")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = """
        CREATE VIEW %s AS (
        SELECT 
        MIN(A.id) as id, 
        A.cpo_name AS cpo_name,
        sum(cast(A.cpo_times as float8)) AS cpo_times,
        sum(cast(A.cpo_late as float8)) AS cpo_late,
        sum(cast(A.cpo_early as float8)) AS cpo_early,
        sum(cast(A.cpo_absence as float8)) AS cpo_absence,
        sum(cast(A.cpo_leave as float8)) AS cpo_leave
        FROM cpo_cpo_attendance AS A
        GROUP BY A.cpo_name)
        """%self._table

        self.env.cr.execute(query)


# class Report_work_record(models.AbstractModel):
#     _name = 'report.cpo_attendance.report_for_work_record'
#
#     @api.model
#     def render_html(self, docids, data=None):
#         report_obj = self.env['report']
#         a = self.env['cpo.attendance_sql'].init()
#
#         docs = self.env['cpo.attendance_sql'].browse(docids)
#         # data 是一个大型的字典 忘了可以 print看看里面有什么
#         if data:
#             if len(data['form']['name']) == 2:
#                 docs = self.env['work.work_record'].search([
#                     ('name', '=', data['form']['name'][0]),
#                     ('day', '>=', data['form']['start_time']),
#                     ('day', '<=', data['form']['end_time'])])
#             else:
#                 docs = self.env['work.work_record'].search([
#                     ('name', 'in', data['form']['name']),
#                     ('day', '>=', data['form']['start_time']),
#                     ('day', '<=', data['form']['end_time'])])
#         docargs = {
#             'doc_ids': docids,
#             'doc_model': 'cpo.attendance_sql',
#             'docs': docs,
#
#         }
#         return report_obj.render('cpo_attendance.report_for_work_record', docargs)
