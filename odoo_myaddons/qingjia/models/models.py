# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from decimal import Decimal
from odoo.exceptions import ValidationError

#请假单
class qingjia1(models.Model):
    _name = 'qingjia.qingjiadan'
    _description = u'请假单'

    yuangong_user = fields.Many2one('hr.employee', u'申请人',required=1)        #hr.employee
    manager = fields.Many2one('hr.employee',u'申请对象',required=1,domain=[('department_id','=','hr')])    #利用domain限制选取
    start_time = fields.Datetime(u'开始时间',required=1)
    end_time = fields.Datetime(u'结束时间',required=1)
    days = fields.Char(u'天数',compute='_d')
    types = fields.Selection([
        ("things","事/病假"),
        ("change","调休"),
    ],string="休假类型",required=1)
    reason = fields.Text(u'请假理由',required=0)
    state = fields.Selection([
        ('draft','草稿'),
        ('confirm',"已提交"),
        ('approval','已审批'),
        ('cancel','已取消')
    ],u'状态',required=0,default='draft')

    aggrement = fields.Selection([
        ("yes","同意"),
        ("no","拒绝"),
    ],string="是否同意申请")
    unreason = fields.Text(u'拒绝理由',required=0)
    deal = fields.Char(u'是否已处理',compute='_deal')
    deco = fields.Char(u'着色',compute='_deal')

    #对请假时长的约束警告
    @api.constrains('end_time')
    # def _e(self):
    #     for record in self:
    #         from_dt = fields.Datetime.from_string(record.start_time)
    #         # from_dt = datetime.datetime.strptime(record.start_time,"%Y-%m-%d %H:%M:%S")
    #         to_dt = fields.Datetime.from_string(record.end_time)
    #         # to_dt = datetime.datetime.strptime(record.end_time,"%Y-%m-%d %H:%M:%S")
    #         if to_dt <= from_dt:
    #             raise ValidationError("结束时间必须大于开始时间")
    #         elif to_dt.day == from_dt.day:
    #             if to_dt.hour - from_dt.hour <4:
    #                 raise ValidationError('请假时长必须大于4个小时')
    #             elif to_dt.hour - from_dt.hour ==4 and to_dt.minute<from_dt.minute:
    #                 raise ValidationError('请假时长必须大于4个小时')
    #             elif to_dt.hour - from_dt.hour ==4 and to_dt.minute==from_dt.minute and to_dt.second<from_dt.second:
    #                 raise ValidationError('请假时长必须大于4个小时')
    #         elif to_dt.day - from_dt.day == 1:
    #             if to_dt.hour + (24 - from_dt.hour) <4:
    #                 raise ValidationError('请假时长必须大于4个小时')
    #             elif to_dt.hour - from_dt.hour ==4 and to_dt.minute<from_dt.minute:
    #                 raise ValidationError('请假时长必须大于4个小时')
    #             elif to_dt.hour - from_dt.hour ==4 and to_dt.minute==from_dt.minute and to_dt.second<from_dt.second:
    #                 raise ValidationError('请假时长必须大于4个小时')
    #         else:
    #             continue
    #对请假时间点的约束
    @api.constrains('start_time','end_time')
    # def _f(self):
    #     for record in self:
    #         from_dt = datetime.datetime.strptime(record.start_time, "%Y-%m-%d %H:%M:%S")
    #         to_dt = datetime.datetime.strptime(record.end_time, "%Y-%m-%d %H:%M:%S")
    #         if datetime.datetime(from_dt.year,from_dt.month,from_dt.day,8) < from_dt < datetime.datetime(from_dt.year,from_dt.month,from_dt.day,12):
    #             raise ValidationError('请假开始时间必须在上午8点前或在中午12点到2点间')
    #         elif from_dt>datetime.datetime(from_dt.year,from_dt.month,from_dt.day,14):
    #             raise ValidationError('请假开始时间必须在上午8点前或在中午12点到2点间')
    #         if to_dt < datetime.datetime(to_dt.year,to_dt.month,to_dt.day,12):
    #             raise ValidationError('请假结束时间必须在中午12点到2点间或下午6点后')
    #         elif datetime.datetime(to_dt.year,to_dt.month,to_dt.day,14) < to_dt <datetime.datetime(to_dt.year,to_dt.month,to_dt.day,18):
    #             raise ValidationError('请假结束时间必须在中午12点到2点间或下午6点后')


    #计算请假days天数
    @api.depends('start_time','end_time')
    @api.multi
    def _d(self):
        for record in self:
            # time_delta = datetime.datetime.strptime(record.end_time,"%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(record.start_time,"%Y-%m-%d %H:%M:%S")
            # record.days = str(int(time_delta.days)+1)
            # record.days = str(int(time_delta.days) + float(time_delta.seconds) / 86400)
            from_dt = fields.Datetime.from_string(record.start_time)
            to_dt = fields.Datetime.from_string(record.end_time)
            time_delta = to_dt - from_dt
            record.days = time_delta.days + float(time_delta.seconds) / 86400
            record.days = Decimal(record.days).quantize(Decimal('0.00'))

    #判断是否已处理(deal)
    @api.depends('aggrement')
    @api.multi
    def _deal(self):
        for record in self:
            if record.aggrement and record.state != 'confirm':
                record.deal = "已处理"
                record.deco = False
            elif record.state == 'cancel':
                record.deal = '已处理'
                record.deco = False
            else:
                record.deal = "未处理"
                record.deco = True

    # @api.multi
    # def do_draft(self):
    #     self.state = 'draft'

    @api.multi
    def do_confirm(self):
        self.state = 'confirm'

    @api.multi
    def have_approval(self):
        self.state = 'approval'
        # if self.aggrement:
        #     self.state = 'approval'
        # else:
        #     self.state = 'confirm'

    @api.multi
    def do_cancel(self):
        self.state = 'cancel'
        self.aggrement = 'no'
