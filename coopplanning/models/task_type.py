# -*- coding: utf-8 -*-

from odoo import api, fields, models

    
class TaskType(models.Model):
    _description = 'TaskType'
    _name = 'coopplanning.task_type'
    
    name = fields.Char(string='Task Type Name', required=True)