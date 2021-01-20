# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CpoWizard(models.TransientModel):
    _name = 'cpo.wizard'

    cpo_name = fields.Many2one('hr.employee', u'员工姓名')
    cpo_id = fields.Char(u'员工ID', compute='_search_id')
    cpo_day = fields.Date(u'上班日期', required=1)

    # @api.depends('cpo_name')
    # @api.multi
    # def _search_id(self):
    #     for record in self:
    #         record.cpo_id = record.cpo_name.id

    @api.multi
    def a(self):
        self.env['cpo.cpo_time'].create({
            'cpo_name':self.cpo_name.name,
            'cpo_id':self.cpo_name.id,
            'cpo_day':self.cpo_day,
        })