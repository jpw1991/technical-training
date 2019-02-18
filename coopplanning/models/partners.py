# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _description = 'Partner'
    _name = 'coopplanning.partner'
    
    name = fields.Char(string='Partner Name', required=True)