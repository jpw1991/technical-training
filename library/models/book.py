# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Book(models.Model):
    _description = 'Book'
    _name = 'library.book'
    
    name = fields.Char(string='Author Name', required=True)
    author_id = fields.Many2many('library.author', string='Authors', ondelete='restrict')