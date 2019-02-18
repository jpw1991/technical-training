# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Author(models.Model):
    _description = 'Author'
    _name = 'library.author'
    
    name = fields.Char(string='Author Name', required=True)