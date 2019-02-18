# -*- coding: utf-8 -*-

from odoo import api, fields, models

    
class Task(models.Model):
    _description = 'Task'
    _name = 'coopplanning.task'
    
    name = fields.Char(string='Task Name', required=True)
    
    #task_id = fields.One2many('coopplanning.task_type', 'task_type_id', string='Task template')
    task_type_id = fields.Many2one('coopplanning.task_type')
    partner_ids = fields.Many2many('coopplanning.partner')