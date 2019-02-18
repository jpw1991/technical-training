# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Course(models.Model):
    _description = 'Course'
    _name = 'openacademy.course'
    
    name = fields.Char(string='Course Name', required=True)
    level = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], default='medium')

class Partner(models.Model):
    _description = 'Partner'
    _name = 'openacademy.partner'
    
    name = fields.Char(string='Partner Name', required=True)
    is_instructor = fields.Boolean(default=False)

class Session(models.Model):
    _description = 'Session'
    _name = 'openacademy.session'
    
    name = fields.Char(string='Session Name', required=True)
    teacher_id = fields.Many2one('openacademy.partner', string='Teacher', ondelete='cascade')
    course_id = fields.Many2one('openacademy.course', string='Course', ondelete='cascade')
    preparations = fields.Selection([
        ('in_preparation', 'In Preparation'),
        ('ready', 'Ready'),
        ('archived', 'Archived'),
    ], default='in_preparation')
    