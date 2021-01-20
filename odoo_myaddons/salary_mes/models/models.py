# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# import datetime

class salary_mes(models.Model):
    _name = 'sa.message'

    employee_name = fields.Many2one('hr.employee',u'员工姓名',required=1)
    employee_id = fields.Char(u'员工ID',compute='_search_id')
    employee_salary = fields.Char(u'员工工资',required=1)
    mes = fields.Text(u'备注',required=0)
    # write_time = fields.Datetime(u'创建时间')

    #获得员工ID
    @api.depends('employee_name')
    @api.multi
    def _search_id(self):
        for record in self:
            record.employee_ID = record.employee_name.id

    #对工资的类型进行约束
    @api.constrains('employee_salary')
    def Constrant(self):
        for record in self:
            salary = record.employee_salary
            try:
                float(salary)
                pass
            except:
                raise ValidationError('“员工工资”栏请输入数字')

    #避免重复输入
    # @api.constrains('employee_id')
    # def Constrant(self):
    #     for record in self:
    #         a = self.search(
    #             [('employee_id', '=', record.employee_name.id)])
    #         if len(a) >= 1:
    #             raise ValidationError('该员工记录已存在')

    # def get_time(self):
    #     pass
