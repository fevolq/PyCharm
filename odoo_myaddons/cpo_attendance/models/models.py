# -*- coding: utf-8 -*-
from __future__ import division
from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError

#排班
class cpo_time(models.Model):
    _name = 'cpo.cpo_time'

    cpo_name = fields.Many2one('hr.employee', u'员工姓名')
    cpo_id = fields.Char(u'员工ID',compute='_search_id')
    cpo_day = fields.Date(u'上班日期',required=1)
    # work_time = fields.Selection([
    #     ('am 8 - pm 6','上午8点——下午6点'),
    #     ('pm 8 - am 6','下午8点——早上6点')
    # ],u'上班时间段',default="am 8 - pm 6")
    work_time = fields.Char(U'上班时间段',default = '上午8点——下午6点')
    # day_night = fields.Char(u'白班或晚班',compute='_select')

    # @api.depends('work_time')
    # @api.multi
    # def _select(self):
    #     for record in self:
    #         if record.work_time == '上午8点——下午6点':
    #             record.day_night = '白班'
    #         else:
    #             record.day_night = '晚班'

    @api.depends('cpo_name')
    @api.multi
    def _search_id(self):
        for record in self:
            record.cpo_id = record.cpo_name.id

#打卡
class cpo_click(models.Model):
    _name = 'cpo.cpo_click'

    cpo_test = fields.Many2one('hr.employee',u'打卡人')
    cpo_id = fields.Char(u'员工ID')
    cpo_name = fields.Char(u'员工姓名')
    cpo_day = fields.Date(u'打卡日期')
    # cpo_start_time = fields.Datetime(u'签到时间',required=0)
    # cpo_end_time = fields.Datetime(u'签退时间',required=0)
    cpo_click_time = fields.Datetime(u'打卡时间', required=0)
    cpo_states = fields.Selection([
        ('no_click','未打卡'),
        ('have_click','已打卡'),
    ],u'打卡状态',required = 0,default='no_click')
    #打卡按钮
    def Click(self):
        self.cpo_states = 'have_click'
        self.write({
            'cpo_id': self.cpo_test.id,
            'cpo_name': self.cpo_test.name,
            # 'cpo_click_time':datetime.datetime.now(),
            # 'cpo_day':datetime.datetime.today(),
        })
    # cpo_states = fields.Selection([
    #     ('no_click','未打卡'),
    #     ('have_start','已签到'),
    #     ('have_end','已签退')
    # ],u'签到状态',required=0,default='no_click')
    #
    # #签到
    # def cpo_start(self):
    #     self.cpo_states = 'have_start'
    #     self.write({
    #         'cpo_id': self.cpo_name.cpo_id,
    #         'cpo_name': self.cpo_name.name,
    #         # 'cpo_start_time': datetime.datetime.now(),
    #         # 'cpo_day':datetime.datetime.today(),
    #     })
    # #签退
    # def cpo_end(self):
    #     self.cpo_states = 'have_end'
    #     self.write({
    #         'cpo_id': self.cpo_name.cpo_id,
    #         'cpo_name': self.cpo_name.name,
    #         # 'cpo_end_time': datetime.datetime.now(),
    #         # 'cpo_day': datetime.datetime.today(),
    #     })

    @api.constrains('cpo_name')
    def Constrant(self):
        for record in self:
            now = datetime.datetime.now()
            now_day = datetime.datetime(now.year,now.month,now.day)
            a =  self.search([('cpo_name','=',record.cpo_test.name),('cpo_day','=',now_day.strftime("%Y-%m-%d %H:%M:%S"))])
            if now < datetime.datetime(now.year,now.month,now.day,12):
                if len(a) >= 3:
                    raise ValidationError('您上午已打卡签到和签退')


#考勤表（行记录是上一个月每人每天的记录）
class cpo_attendance(models.Model):
    _name = 'cpo.cpo_attendance'
    _description = u'考勤表'

    cpo_inh = fields.Many2one('hr.employee',u'继承')
    cpo_id = fields.Char(u'员工ID')
    cpo_name = fields.Char(u'员工姓名')
    cpo_day = fields.Date(u'日期')
    cpo_work_time = fields.Char(u'上班时间段')
    cpo_start1 = fields.Char(u'卡1')
    cpo_end1 = fields.Char(u'卡2')
    cpo_start2 = fields.Char(u'卡3')
    cpo_end2 = fields.Char(u'卡4')
    cpo_states = fields.Selection([
        ('0','未生成'),
        ('1','已生成')
    ],u'考勤表生成',default='0')

    cpo_late = fields.Char(u'迟到（分钟）',default='0',compute='Depends',store=True)
    cpo_early = fields.Char(u'早退（分钟）',dafault='0',compute='Depends',store=True)
    cpo_absence = fields.Char(u'缺勤（天）',default='0',compute='Depends',store=True)
    cpo_leave = fields.Char(u'请假（天）',default='0',compute='Depends',store=True)

    cpo_times = fields.Char(u"当日工时（小时）",compute='Depends',store=True)    #一天满记8小时
    color = fields.Integer(u'Color Index')

    #计算工时
    @api.depends('cpo_name','cpo_day','cpo_work_time','cpo_start1','cpo_end1','cpo_start2','cpo_end2',)
    @api.multi
    def Depends(self):
        for record in self:
            try:
                day_time = datetime.datetime.strptime(record.cpo_day,'%Y-%m-%d')    #单行指定的日期
                employee_name = record.cpo_name     #单行的人名

                date_time = datetime.datetime(day_time.year,day_time.month,1)   #要查找的记录的年份和月份，可在指定查找请假月份时使用
                qingjia_dic = self.qingjia_time(employee_name,date_time)    #这个人的指定月份的请假记录（集合）

                #当天的上下班时间点
                am_start = datetime.datetime(day_time.year,day_time.month,day_time.day,8)
                am_end = datetime.datetime(day_time.year,day_time.month,day_time.day,12)
                pm_start = datetime.datetime(day_time.year,day_time.month,day_time.day,14)
                pm_end = datetime.datetime(day_time.year, day_time.month, day_time.day, 18)

                if record.cpo_start1 and not record.cpo_start2:
                    start1 = datetime.datetime.strptime(record.cpo_start1,'%Y-%m-%d %H:%M:%S')
                    end1 = datetime.datetime.strptime(record.cpo_end1, '%Y-%m-%d %H:%M:%S')
                elif record.cpo_start1 and record.cpo_start2:
                    start1 = datetime.datetime.strptime(record.cpo_start1, '%Y-%m-%d %H:%M:%S')
                    end1 = datetime.datetime.strptime(record.cpo_end1, '%Y-%m-%d %H:%M:%S')
                    start2 = datetime.datetime.strptime(record.cpo_start2, '%Y-%m-%d %H:%M:%S')
                    end2 = datetime.datetime.strptime(record.cpo_end2, '%Y-%m-%d %H:%M:%S')

                if record.cpo_work_time == u'无排班':  #无排班
                    record.cpo_late = '0'
                    record.cpo_early = '0'
                    record.cpo_absence = '0'
                    record.cpo_leave = '0'
                    record.cpo_times = '0'
                else:   #有排班
                    if "a{}".format(day_time.day) in qingjia_dic:   #当天在请假集合内能找到，有请假
                        if qingjia_dic['a{}'.format(day_time.day)] <= am_start:     #请假开始于上午
                            if qingjia_dic['b{}'.format(day_time.day)] >= pm_end:   #请假结束于下午，即请整天假
                                record.cpo_leave = '1'
                                record.cpo_times = '0'
                            else:   #请一上午假
                                record.cpo_leave = '0.5'
                                if not record.cpo_start1:   #下午无打卡
                                    record.cpo_absence = '0.5'
                                    record.cpo_times = '0'
                                else:   #下午有打卡
                                    if start1 <= pm_start:   #下午没迟到
                                        if end1 <= pm_start:     #打卡无效
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '0'
                                        elif end1 >= pm_end:     #下午没早退
                                            record.cpo_times = '4'
                                        else:   #下午早退
                                            # record.cpo_early = '下午早退{}分钟'.format((pm_end-end1).seconds/60)
                                            record.cpo_early = '{}'.format((pm_end - end1).seconds / 60)
                                            record.cpo_times = '{}'.format(4-round((pm_end-end1).seconds/3600,2))
                                    elif pm_start < start1 < pm_end:     #下午迟到
                                        # record.cpo_late = '下午迟到{}分钟'.format((start1-pm_start).seconds/60)
                                        record.cpo_late = '{}'.format((start1 - pm_start).seconds / 60)
                                        if end1 < pm_end:    #下午早退
                                            # record.cpo_early = '下午早退{}分钟'.format((pm_end-end1).seconds/60)
                                            record.cpo_early = '{}'.format((pm_end - end1).seconds / 60)
                                            record.cpo_times = '{}'.format(4-round((start1-pm_start).seconds/3600,2)-round((pm_end-end1).seconds/3600,2))
                                        else:   #下午没早退
                                            record.cpo_times = '{}'.format(4-round((start1-pm_start).seconds/3600,2))
                                    else:   #打卡无效
                                        record.cpo_absence = '0.5'
                                        record.cpo_times = '0'
                        elif am_end <= qingjia_dic['a{}'.format(day_time.day)] <=pm_start:  #请假开始于下午，则只可能请一下午假
                            record.cpo_leave = '0.5'
                            if start1 <= am_start:   #上午没迟到
                                if end1 <= am_start:     #打卡无效
                                    record.cpo_absence = '0.5'
                                    record.cpo_times = '0'
                                elif end1 >= am_end:     #上午没早退
                                    record.cpo_times = '4'
                                else:   #上午早退
                                    # record.cpo_early = '上午早退{}分钟'.format((am_end-end1).seconds/60)
                                    record.cpo_early = '{}'.format((am_end - end1).seconds / 60)
                                    record.cpo_times = '{}'.format(4-round((am_end-end1).seconds/3600,2))
                            elif am_start < start1 < am_end:     #上午迟到
                                # record.cpo_late = '上午迟到{}分钟'.format((start1-am_start).seconds/60)
                                record.cpo_late = '{}'.format((start1 - am_start).seconds / 60)
                                if end1 >= am_end:   #上午没早退
                                    record.cpo_times = '{}'.format(4-round((start1-am_start).seconds/3600,2))
                                else:  #上午早退
                                    # record.cpo_early = '上午早退{}分钟'.format((am_end-end1).seconds/60)
                                    record.cpo_early = '{}'.format((am_end - end1).seconds / 60)
                                    record.cpo_times = '{}'.format(4-round((am_end-end1).seconds/3600,2)-round((start1-am_start).seconds/3600,2))
                            else:   #打卡无效
                                record.cpo_absence = '0.5'
                                record.cpo_times = '0'
                    else:   #无请假
                        if not record.cpo_start1:   #没有打卡，则缺勤
                            record.cpo_absence = '1'
                            record.cpo_times = '0'
                        else:   #有打卡，判断打卡时间
                            if not record.cpo_start2:   #只有两个打卡
                                if start1 < am_end <= end1:    #一个在上午一个在下午
                                    if start1 <= am_start:   #上午没迟到
                                        if end1 >= pm_end:       #下午没早退
                                            record.cpo_times = '8'
                                        elif pm_start < end1 < pm_end:  #下午早退
                                            delta = (pm_end - end1).seconds  #秒
                                            # record.cpo_early = '下午早退{}分钟'.format(delta/60)
                                            record.cpo_early = '{}'.format(delta / 60)
                                            record.cpo_times = '{}'.format(8-round(delta/3600,2))
                                        else:   #下午缺勤
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '4'
                                    else:  #上午迟到
                                        delta1 = (start1-am_start).seconds
                                        # record.cpo_late = '上午迟到{}分钟'.format(delta1/60)
                                        record.cpo_late = '{}'.format(delta1 / 60)
                                        if record.cpo_end1 >= pm_end:
                                            record.cpo_times = '{}'.format(8-round(delta1/3600,2))
                                        elif end_start < end1 < pm_end:
                                            delta2 = (pm_end - end1).seconds
                                            # ecord.cpo_early = '下午早退{}分钟'.format(delta2 / 60)
                                            cord.cpo_early = '{}'.format(delta2 / 60)
                                            record.cpo_times = '{}'.format(8 - round(delta1 / 3600,2)-round(delta2/3600,2))
                                        else:
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '{}'.format(4-round(delta1/3600,2))
                                elif end1 < am_end:     #两个都在上午
                                    delta3 = (am_end - end1).seconds
                                    # record.cpo_early = '上午早退{}分钟'.format(delta3/60)
                                    record.cpo_early = '{}'.format(delta3 / 60)
                                    record.cpo_absence = '0.5'
                                    if end1 <= am_start:     #缺勤
                                        record.cpo_absence = '1'
                                        record.cpo_times = '0'
                                    elif start1 <= am_start < end1:    #没迟到
                                        record.cpo_times = '{}'.format(4-round(delta3/3600,2))
                                    else:  #上午迟到早退
                                        delta4 = (start1-am_start).seconds
                                        # record.cpo_late = '上午迟到{}分钟'.format(delta4/60)
                                        record.cpo_late = '{}'.format(delta4 / 60)
                                        record.cpo_times = '{}'.format(4-round(delta3/3600,2)-round(delta4/3600,2))
                                else:   #两个都在下午
                                    record.cpo_absence = '0.5'
                                    if end1 <= pm_start or start1>=pm_end:
                                        record.cpo_absence = '1'
                                        record.cpo_times = '0'
                                    elif start1 <= pm_start and end1<=pm_end:     #下午早退
                                        delta5 = (pm_end-end1).seconds
                                        # record.cpo_early = '下午早退{}分钟'.format(delta5/60)
                                        record.cpo_early = '{}'.format(delta5 / 60)
                                        record.cpo_times = '{}'.format(4-round(delta5/3600,2))
                                    elif start1>pm_start and end1>=pm_end:    #下午迟到
                                        delta6 = (start1-pm_start).seconds
                                        # record.cpo_late = '下午迟到{}分钟'.format(delta6/60)
                                        record.cpo_late = '{}'.format(delta6 / 60)
                                        record.cpo_times = '{}'.format(4-round(delta6/3600,2))
                                    else:   #下午迟到早退
                                        delta7 = (start1-pm_start).seconds
                                        delta8 = (pm_end-end1).seconds
                                        # record.cpo_late = '下午迟到{}分钟'.format(delta7/60)
                                        record.cpo_late = '{}'.format(delta7 / 60)
                                        # record.cpo_early = '下午早退{}分钟'.format(delta8/60)
                                        record.cpo_early = '{}'.format(delta8 / 60)
                                        record.cpo_times = '{}'.format(round((end1-start1).seconds/3600,2))
                            else:   #有4个打卡
                                if end1 <= am_start or start1 >= am_end:     #上午缺勤
                                    record.cpo_absence = '0.5'
                                    if start2 <= pm_start:    #下午没迟到
                                        if end2 >= pm_end:       #下午没早退
                                            record.cpo_times = '4'
                                        elif end2 <= pm_start:
                                            record.cpo_absence = '1'
                                            record.cpo_times = '0'
                                        else:
                                            # record.cpo_early = '下午早退{}分钟'.format((pm_end-end2).seconds/60)
                                            record.cpo_early = '{}'.format((pm_end - end2).seconds / 60)
                                            record.cpo_times = '{}'.format(4-round((pm_end-end2).seconds/3600,2))
                                    elif pm_start < start2 < pm_end:  #下午迟到
                                        # record.cpo_late = '下午迟到{}分钟'.format((start2-pm_start).seconds/60)
                                        record.cpo_late = '{}'.format((start2 - pm_start).seconds / 60)
                                        if record.cpo_end2 >= pm_end:  # 下午没早退
                                            record.cpo_times = '{}'.format(4-round((start2-pm_start).seconds/3600,2))
                                        else:  #下午早退
                                            # record.cpo_early = '下午早退{}分钟'.format((pm_end-end2).seconds/60)
                                            record.cpo_early = '{}'.format((pm_end - end2).seconds / 60)
                                            record.cpo_times = '{}'.format(4-round((start2-pm_start).seconds/3600,2)-round((start2-pm_start).seconds/3600,2))
                                    else:   #下午缺勤
                                        record.cpo_absence = '1'
                                        record.cpo_times = '0'
                                elif start1 <= am_start:     #上午没迟到
                                    if end1 >= am_end:   #上午正常
                                        if start2 <= pm_start:    #下午没迟到
                                            if end2 >= pm_end:       #下午没早退
                                                record.cpo_times = '8'
                                            elif end2 <= pm_start:
                                                record.cpo_absence = '0.5'
                                                record.cpo_times = '4'
                                            else:
                                                # record.cpo_early = '下午早退{}分钟'.format((pm_end-end2).seconds/60)
                                                record.cpo_early = '{}'.format((pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8-round((pm_end-end2).seconds/3600,2))
                                        elif pm_start < start2 < pm_end:  #下午迟到
                                            # record.cpo_late = '下午迟到{}分钟'.format((start2-pm_start).seconds/60)
                                            record.cpo_late = '{}'.format((start2 - pm_start).seconds / 60)
                                            if end2 >= pm_end:  # 下午没早退
                                                record.cpo_times = '{}'.format(8-round((start2-pm_start).seconds/3600,2))
                                            else:  #下午早退
                                                # record.cpo_early = '下午早退{}分钟'.format((pm_end-end2).seconds/60)
                                                record.cpo_early = '{}'.format((pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8-round((start2-pm_start).seconds/3600,2)-round((start2-pm_start).seconds/3600,2))
                                        else:   #下午缺勤
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '4'
                                    else:  #上午早退
                                        # record.cpo_early = '上午早退{}分钟'.format((am_end-end1).seconds/60)
                                        record.cpo_early = '{}'.format((am_end - end1).seconds / 60)
                                        if start2 <= pm_start:    #下午没迟到
                                            if end2 >= pm_end:       #下午没早退
                                                record.cpo_times = '{}'.format(8-(am_end-end1).seconds/60)
                                            elif end2 <= pm_start:
                                                record.cpo_absence = '0.5'
                                                record.cpo_times = '{}'.format(4-(am_end-end1).seconds/60)
                                            else:
                                                # record.cpo_early = '上午早退{}分钟,下午早退{}分钟'.format((am_end-end1).seconds/60,(pm_end-end2).seconds/60)
                                                record.cpo_early = '{}'.format((am_end - end1).seconds / 60 + (pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8-round((pm_end-end2).seconds/3600,2)-round((am_end-end2).seconds/3600,2))
                                        elif pm_start < start2 < pm_end:  #下午迟到
                                            # record.cpo_late = '下午迟到{}分钟'.format((start2-pm_start).seconds/60)
                                            record.cpo_late = '{}'.format((start2 - pm_start).seconds / 60)
                                            if end2 >= pm_end:  # 下午没早退
                                                record.cpo_times = '{}'.format(8-round((start2-pm_start).seconds/3600,2)-round((am_end-end2).seconds/3600,2))
                                            else:  #下午早退
                                                # record.cpo_early = '上午早退{}分钟,下午早退{}分钟'.format((am_end-end1).seconds/60,(pm_end-end2).seconds/60)
                                                record.cpo_early = '{}'.format((am_end - end1).seconds / 60 + (pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8-round((start2-pm_start).seconds/3600,2)-round((am_end-end2).seconds/3600,2)-round((start2-pm_start).seconds/3600,2))
                                        else:   #下午缺勤
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '{}'.format(4-round((am_end-end2).seconds/3600,2))
                                elif am_start < start1 < am_end:     #上午迟到
                                    # record.cpo_late = '上午迟到{}分钟'.format((start1-am_start).seconds/60)
                                    record.cpo_late = '{}'.format((start1 - am_start).seconds / 60)
                                    if end1 < am_end:     #上午早退
                                        # record.cpo_early = '上午早退{}分钟'.format((am_end-end1).seconds/60)
                                        record.cpo_early = '{}'.format((am_end - end1).seconds / 60)
                                        if start2 <= pm_start:  # 下午没迟到
                                            if end2 >= pm_end:  # 下午没早退
                                                record.cpo_times = '{}'.format(8-round((start1-am_start).seconds/3600,2)-round((am_end-end1).seconds/3600,2))
                                            elif end2 <= pm_start:
                                                record.cpo_absence = '0.5'
                                                record.cpo_times = '{}'.format(4-round((start1-am_start).seconds/3600,2)-round((am_end-end1).seconds/3600,2))
                                            else:
                                                # record.cpo_early = '上午早退{}分钟，下午早退{}分钟'.format((am_end-end1).seconds/60,(pm_end - end2).seconds / 60)
                                                record.cpo_early = '{}'.format((am_end - end1).seconds / 60 + (pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8 - round((start1-am_start).seconds/3600,2)-round((am_end-end1).seconds/3600,2)-round((pm_end - end2).seconds / 3600, 2))
                                        elif pm_start < start2 < pm_end:  # 下午迟到
                                            # record.cpo_late = '上午迟到{}分钟，下午迟到{}分钟'.format((start1-am_start)/60,(start2 - pm_start).seconds / 60)
                                            record.cpo_late = '{}'.format((start1 - am_start).seconds / 60 + (start2 - pm_start).seconds / 60)
                                            if end2 >= pm_end:  # 下午没早退
                                                record.cpo_times = '{}'.format(8 -round((start1-am_start).seconds/3600,2)-round((am_end-end1).seconds/3600,2)- round((start2 - pm_start).seconds / 3600, 2))
                                            else:  # 下午早退
                                                # record.cpo_early = '上午早退{}分钟，下午早退{}分钟'.format((am_end-end1).seconds/60,(pm_end - end2).seconds / 60)
                                                record.cpo_early = '{}'.format((am_end - end1).seconds / 60 + (pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8 - round((start2 - pm_start).seconds / 3600, 2) - round((start2 - pm_start).seconds / 3600, 2)-round((start1-am_start).seconds/3600,2)-round((am_end-end1).seconds/3600,2))
                                        else:  # 下午缺勤
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '{}'.format(4-round((start1-am_start).seconds/3600,2)-round((am_end-end1).seconds/3600,2))
                                    else:   #上午没早退
                                        if start2 <= pm_start:  # 下午没迟到
                                            if end2 >= pm_end:  # 下午没早退
                                                record.cpo_times = '{}'.format(8 - round((start1 - am_start).seconds / 3600, 2))
                                            elif end2 <= pm_start:
                                                record.cpo_absence = '0.5'
                                                record.cpo_times = '{}'.format(4 - round((start1 - am_start).seconds / 3600, 2))
                                            else:
                                                # record.cpo_early = '下午早退{}分钟'.format((pm_end - end2).seconds / 60)
                                                record.cpo_early = '{}'.format((pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8 - round((start1 - am_start).seconds / 3600, 2) - round((pm_end - end2).seconds / 3600, 2))
                                        elif pm_start < start2 < pm_end:  # 下午迟到
                                            # record.cpo_late = '上午迟到{}分钟，下午迟到{}分钟'.format((start1 - am_start).seconds / 60,(start2 - pm_start).seconds / 60)
                                            record.cpo_late = '{}'.format((start1 - am_start).seconds / 60 + (start2 - pm_start).seconds / 60)
                                            if record.cpo_end2 >= pm_end:  # 下午没早退
                                                record.cpo_times = '{}'.format(8 - round((start1 - am_start).seconds / 3600, 2) - round((start2 - pm_start).seconds / 3600, 2))
                                            else:  # 下午早退
                                                # record.cpo_early = '下午早退{}分钟'.format((pm_end - end2).seconds / 60)
                                                record.cpo_early = '{}'.format((pm_end - end2).seconds / 60)
                                                record.cpo_times = '{}'.format(8 - round((start2 - pm_start).seconds / 3600, 2) - round((start2 - pm_start).seconds / 3600, 2) - round((start1 - am_start).seconds / 3600, 2))
                                        else:  # 下午缺勤
                                            record.cpo_absence = '0.5'
                                            record.cpo_times = '{}'.format(4 - round((start1 - am_start).seconds / 3600, 2))
            except Exception as e:
                print(e)
                # raise e

    # 查找某个人某个月的请假记录
    def qingjia_time(self,name,time):   #传入名字和时间(datetime格式)
        """返回为{'a1':1号的请假开始时间,'b1':1号的请假的结束时间,'a2':2号的请假开始时间,'b2':2号的请假的结束时间,···}，x号有请假，就有ax和bx，
        key为str格式，value为datetime格式"""
        li = self.env['qingjia.qingjiadan'].search([('aggrement','=','yes'),('yuangong_user','=',name)])    #这个人的所有“已同意”的请假记录（合集）
        if time.month == 12:     #1月
            time_start = datetime.datetime(time.year,12,1)           #传入时间的当月的开始时间
            time_end = datetime.datetime(time.year,12,31,23,59,59)   #传入时间的当月的结束时间
        else:
            time_start = datetime.datetime(time.year,time.month,1)
            time_end = datetime.datetime(time.year,time.month+1,1)-datetime.timedelta(0,1)

        qingjia_dic = {}
        for i in li:
            qingjia_start = datetime.datetime.strptime(i.start_time, "%Y-%m-%d %H:%M:%S")   #单条记录的请假开始时间
            qingjia_end = datetime.datetime.strptime(i.end_time, "%Y-%m-%d %H:%M:%S")   #同一条记录的请假结束时间
            if qingjia_start>=time_start and qingjia_end<=time_end:     #请假时间开始并结束于这个月内
                if qingjia_end.day == qingjia_start.day:    #同一天
                    qingjia_dic["a{}".format(qingjia_start.day)] = qingjia_start     #当天的请假开始时间
                    qingjia_dic["b{}".format(qingjia_end.day)] = qingjia_end         #当天的请假结束时间
                elif qingjia_end.day - qingjia_start.day == 1:  #相邻
                    qingjia_dic["a{}".format(qingjia_start.day)] = qingjia_start
                    qingjia_dic["b{}".format(qingjia_start.day)] = datetime.datetime(qingjia_start.year,qingjia_start.month,qingjia_start.day,18)  #每天的下班时间
                    qingjia_dic["a{}".format(qingjia_end.day)] = datetime.datetime(qingjia_start.year,qingjia_start.month,qingjia_end.day,8)    #每天的上班时间
                    qingjia_dic["b{}".format(qingjia_end.day)] = qingjia_end
                else:   #相隔n天
                    qingjia_dic["a{}".format(qingjia_start.day)] = qingjia_start
                    qingjia_dic["b{}".format(qingjia_start.day)] = datetime.datetime(qingjia_start.year,qingjia_start.month,qingjia_start.day,18)
                    qingjia_dic["a{}".format(qingjia_end.day)] = datetime.datetime(qingjia_start.year,qingjia_start.month,qingjia_end.day,8)
                    qingjia_dic["b{}".format(qingjia_end.day)] = qingjia_end
                    for n in range(qingjia_start.day+1,qingjia_end.day):
                        qingjia_dic["a{}".format(n)] = datetime.datetime(qingjia_start.year,qingjia_start.month,n,8)
                        qingjia_dic["b{}".format(n)] = datetime.datetime(qingjia_start.year,qingjia_start.month,n,18)
            elif qingjia_start < time_start and time_start <qingjia_end<time_end:   #请假时间开始于这个月前，结束于这个月内
                if qingjia_end.day == 1:    #结束于1号
                    qingjia_dic["a1"] = datetime.datetime(qingjia_end.year,qingjia_end.month,1,8)
                    qingjia_dic["b1"] = qingjia_end
                else:
                    qingjia_dic["a{}".format(qingjia_end.day)] = datetime.datetime(qingjia_end.year,qingjia_end.month,qingjia_end.day,8)
                    qingjia_dic["b{}".format(qingjia_end.day)] = qingjia_end
                    for n in range(1,qingjia_end.day):
                        qingjia_dic["a{}".format(n)] = datetime.datetime(qingjia_end.year, qingjia_end.month, n, 8)
                        qingjia_dic["b{}".format(n)] = datetime.datetime(qingjia_end.year, qingjia_end.month, n, 18)
            elif time_start <qingjia_start<time_end and qingjia_end > time_end:     #请假时间开始于这个月内，结束于这个月后
                if qingjia_start.day == time_end.day:   #开始于这个月的最后一天
                    qingjia_dic["a{}".format(qingjia_start.day)] = qingjia_start
                    qingjia_dic["b{}".format(qingjia_start.day)] = datetime.datetime(qingjia_start.year, qingjia_start.month, qingjia_start.day, 18)
                else:
                    qingjia_dic["a{}".format(qingjia_start.day)] = qingjia_start
                    qingjia_dic["b{}".format(qingjia_end.day)] = datetime.datetime(qingjia_start.year, qingjia_start.month, qingjia_start.day, 18)
                    for n in range(qingjia_start.day+1,time_end.day+1):
                        qingjia_dic["a{}".format(n)] = datetime.datetime(qingjia_start.year, qingjia_start.month, n, 8)
                        qingjia_dic["b{}".format(n)] = datetime.datetime(qingjia_start.year, qingjia_start.month, n, 18)
            elif qingjia_start < time_start and qingjia_end > time_end:     #请假时间开始于这个月前，结束于这个月后，即这整个月都请假
                for n in range(1,time.day+1):
                    qingjia_dic["a{}".format(n)] = datetime.datetime(time.year, time.month, n, 8)
                    qingjia_dic["b{}".format(n)] = datetime.datetime(time.year, time.month, n, 18)
        return qingjia_dic

    # botton按钮，功能：生成对应人的单月考勤表
    def Botton(self):
        # a = self.env['hr.employee'].search([])
        for i in self.env['hr.employee'].search([]):
            self._input(i.name)
        self.cpo_states = '1'  # 改变当前获取的状态

    # 获取上一个月的日期列表
    def _month(self):
        '''上一个月的日期（datetime格式）组成的列表'''
        now = datetime.datetime.now()
        Year = now.year
        Month = now.month  # 现在的月份
        if Month == 1:
            Year = Year - 1
            Month = 12
            Days = (datetime.datetime(Year + 1, 1, 1) - datetime.datetime(Year, Month, 1)).days
        else:
            Month = Month - 1
            Days = (datetime.datetime(Year, Month + 1, 1) - datetime.datetime(Year, Month, 1)).days  # 前一个月的天数
        # return Year,Month,Days     #上一个月的[年份，月份，天数]
        l = []
        for i in range(Days):
            D = datetime.datetime(Year, Month, i + 1)
            l.append(D)
        return l  # 上一个月的日期（datetime格式）的列表

    # 单人单月考勤记录
    def _input(self, name):
        '''写入对应名字的单月的考勤情况'''
        l = self._month()
        for i in l:
            a = self.env['cpo.cpo_click'].search(
                [('cpo_name', '=', name), ('cpo_day', '=', i.strftime("%Y-%m-%d"))])  # 单人单日打卡记录集合
            b = self.env['cpo.cpo_time'].search(
                [('cpo_name', '=', name), ('cpo_day', '=', i.strftime("%Y-%m-%d"))])  # 单人单日的排班记录
            if b:
                c = b[0].work_time  #排班数据
            else:
                c = "无排班"
            if len(a) == 0:
                self.create({
                    'cpo_id': self.env['hr.employee'].search([('name','=',name)])[0].id,
                    'cpo_name': name,
                    'cpo_day': i,
                    'cpo_work_time': c,
                })
            elif len(a) == 2:
                self.create({'cpo_id': self.env['hr.employee'].search([('name','=',name)])[0].id,'cpo_name': name, 'cpo_day': i,
                            'cpo_work_time': c,
                            'cpo_start1': a[0].cpo_click_time, 'cpo_end1': a[1].cpo_click_time, })
            elif len(a) == 4:
                self.create({'cpo_id': self.env['hr.employee'].search([('name','=',name)])[0].id,'cpo_name': name, 'cpo_day': i,
                            'cpo_work_time': c,
                            'cpo_start1': a[0].cpo_click_time, 'cpo_end1': a[1].cpo_click_time,
                            'cpo_start2': a[2].cpo_click_time, 'cpo_end2': a[3].cpo_click_time, })

    # #botton按钮，生成对应人的单月考勤表
    # def a(self):
    #     self._input(self.cpo_name.name)     #传入名字，生成他的上一个月的考勤记录到考勤表内
    #     self.cpo_states = '1'  # 改变当前获取的状态
    #
    #     # a = self.env['cpo.cpo_click'].search([('cpo_name','=','1')])    #打卡表内名字是1的记录的合集
    #     # #a[0].cpo_start_time     #打卡表内名字是2的打卡记录内的第一条的签到时间字段的值
    #     # b = self.env['cpo.cpo_time'].search([('cpo_name','=','1')])
    #     #
    #     # self.write({
    #     #     'cpo_id':self.cpo_name.cpo_id,
    #     #     'cpo_name':self.cpo_name.name,
    #     #     'cpo_day':a[0].cpo_day,
    #     #     'cpo_work_time':b[0].work_time,
    #     #     'cpo_start1':a[0].cpo_start_time,
    #     #     'cpo_end1':a[1].cpo_end_time,
    #     #     # 'cpo_start2':7,
    #     #     # 'cpo_end2':8,
    #     #     # 'cpo_start3':9,
    #     #     # 'cpo_end':0,
    #     # })
    #
    # #获取上一个月的日期列表
    # def _month(self):
    #     '''上一个月的日期（datetime格式）组成的列表'''
    #     now = datetime.datetime.now()
    #     Year = now.year
    #     Month = now.month  #现在的月份
    #     if Month==1:
    #         Year = Year - 1
    #         Month = 12
    #         Days = (datetime.datetime(Year+1,1,1)-datetime.datetime(Year,Month,1)).days
    #     else:
    #         Month = Month - 1
    #         Days = (datetime.datetime(Year,Month+1,1)-datetime.datetime(Year,Month,1)).days     #前一个月的天数
    #     #return Year,Month,Days     #上一个月的[年份，月份，天数]
    #     l = []
    #     for i in range(Days):
    #         D = datetime.datetime(Year,Month,i+1)
    #         l.append(D)
    #     return l    #上一个月的日期（datetime格式）的列表
    #
    # #单人单月考勤记录
    # def _input(self,name):
    #     '''写入对应名字的单月的考勤情况'''
    #     l = self._month()
    #     for i in l:
    #         # i = l[-1]
    #         a = self.env['cpo.cpo_click'].search([('cpo_name', '=',name),('cpo_day','=',i.strftime("%Y-%m-%d"))])   #单人单日打卡记录集合
    #         b = self.env['cpo.cpo_time'].search([('cpo_name', '=',name),('cpo_day','=',i.strftime("%Y-%m-%d"))])    #单人单日的排班记录
    #         if b:
    #             c = b[0].work_time
    #         else:
    #             c = "无排班"
    #         if i == l[0]:
    #             if len(a) == 0:
    #                 self.write({
    #                     'cpo_id': self.cpo_name.cpo_id,
    #                     'cpo_name': self.cpo_name.name,
    #                     'cpo_day': i,
    #                     'cpo_work_time': c,
    #                 })
    #                 # self.write({'cpo_start1':'None','cpo_end1':'None'})
    #                 pass
    #             elif len(a) == 2:
    #                 self.write({'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,})
    #             elif len(a) == 4:
    #                 self.write({'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,
    #                             'cpo_start2':a[2].cpo_start_time,'cpo_end2':a[3].cpo_end_time,})
    #             elif len(a) == 6:
    #                 self.write({'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,
    #                             'cpo_start2':a[2].cpo_start_time,'cpo_end2':a[3].cpo_end_time,
    #                             'cpo_start3':a[4].cpo_start_time,'cpo_end3':a[5].cpo_end_time,})
    #             else:
    #                 self.write({'cpo_id': self.cpo_name.cpo_id, 'cpo_name': self.cpo_name.name, 'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1': '打卡过多', })    #一天内打卡超过6次，还需要进行处理
    #         else:
    #             if len(a) == 0:
    #                 self.create({
    #                     'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,})
    #                 # self.write({'cpo_start1':'None','cpo_end1':'None'})
    #                 pass
    #             elif len(a) == 2:
    #                 self.create({'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,})
    #             elif len(a) == 4:
    #                 self.create({'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,
    #                             'cpo_start2':a[2].cpo_start_time,'cpo_end2':a[3].cpo_end_time,})
    #             elif len(a) == 6:
    #                 self.create({'cpo_id': self.cpo_name.cpo_id,'cpo_name': self.cpo_name.name,'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,
    #                             'cpo_start2':a[2].cpo_start_time,'cpo_end2':a[3].cpo_end_time,
    #                             'cpo_start3':a[4].cpo_start_time,'cpo_end3':a[5].cpo_end_time,})
    #             else:
    #                 self.create({'cpo_id': self.cpo_name.cpo_id, 'cpo_name': self.cpo_name.name, 'cpo_day': i,'cpo_work_time': c,
    #                             'cpo_start1': '打卡过多', })    #一天内打卡超过6次，还需要进行处理
    #         # if i==l[0]:
    #         #     if b:
    #         #         c = b[0].work_time
    #         #         self.write({
    #         #             'cpo_id': self.cpo_name.cpo_id,
    #         #             'cpo_name': self.cpo_name.name,
    #         #             'cpo_day': i,
    #         #             'cpo_work_time': c,
    #         #         })
    #         #     # if len(a) == 0:
    #         #     #     # self.write({'cpo_start1':'None','cpo_end1':'None'})
    #         #     #     pass
    #         #     # elif len(a) == 2:
    #         #     #     self.write({'cpo_start1': a[0].cpo_start_time, 'cpo_end1': a[1].cpo_end_time, })
    #         #     # elif len(a) == 4:
    #         #     #     self.write({'cpo_start1': a[0].cpo_start_time, 'cpo_end1': a[1].cpo_end_time,
    #         #     #                 'cpo_start2': a[2].cpo_start_time, 'cpo_end2': a[3].cpo_end_time, })
    #         #     # elif len(a) == 6:
    #         #     #     self.write({'cpo_start1': a[0].cpo_start_time, 'cpo_end1': a[1].cpo_end_time,
    #         #     #                 'cpo_start2': a[2].cpo_start_time, 'cpo_end2': a[3].cpo_end_time,
    #         #     #                 'cpo_start3': a[4].cpo_start_time, 'cpo_end3': a[5].cpo_end_time, })
    #         #     # else:
    #         #     #     self.write({'cpo_start1': '打卡过多'})  # 一天内打卡超过6次，需要进行处理
    #         #     else:
    #         #         c = '无排班'
    #         #         self.write({
    #         #             'cpo_id': self.cpo_name.cpo_id,
    #         #             'cpo_name': self.cpo_name.name,
    #         #             'cpo_day': i,
    #         #             'cpo_work_time': c,
    #         #         })
    #         # else:
    #         #     if b:
    #         #         c = b[0].work_time
    #         #         self.create({
    #         #             'cpo_id': self.cpo_name.cpo_id,
    #         #             'cpo_name': self.cpo_name.name,
    #         #             'cpo_day': i,
    #         #             'cpo_work_time': c,
    #         #         })
    #         #     else:
    #         #         c = '无排班'
    #         #         self.create({
    #         #             'cpo_id': self.cpo_name.cpo_id,
    #         #             'cpo_name': self.cpo_name.name,
    #         #             'cpo_day': i,
    #         #             'cpo_work_time': c,
    #         #         })
    #         # if len(a) == 0:
    #         #     # self.write({'cpo_start1':'None','cpo_end1':'None'})
    #         #     pass
    #         # elif len(a) == 2:
    #         #     self.write({'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,})
    #         # elif len(a) == 4:
    #         #     self.write({'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,
    #         #                 'cpo_start2':a[2].cpo_start_time,'cpo_end2':a[3].cpo_end_time,})
    #         # elif len(a) == 6:
    #         #     self.write({'cpo_start1':a[0].cpo_start_time,'cpo_end1':a[1].cpo_end_time,
    #         #                 'cpo_start2':a[2].cpo_start_time,'cpo_end2':a[3].cpo_end_time,
    #         #                 'cpo_start3':a[4].cpo_start_time,'cpo_end3':a[5].cpo_end_time,})
    #         # else:
    #         #     self.write({'cpo_start1':'打卡过多'})   #一天内打卡超过6次，还需要进行处理




