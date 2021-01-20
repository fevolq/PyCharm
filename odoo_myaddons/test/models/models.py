# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spider(models.Model):
    _name = 'test.spider'
    _description = u'爬虫网站'

    name = fields.Char(u"网站名称",required=0)
    net = fields.Char(u'网址',required=True)
    net_type = fields.Selection([
        ("photo", "图片"),
        ("message", "信息"),
    ],string="网址类型",required=1)
    whether = fields.Selection([
        ("yes","成功"),
        ("no","不成功"),
    ],string="是否成功",required=1)
    unreason = fields.Text(u'不成功理由', required=0)
