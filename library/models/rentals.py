# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Rental(models.Model):
    _description = 'Rental'
    _name = 'library.rental'
    
    name = fields.Char(string='Rental Name', required=True)
    customer_id = fields.Many2one('library.customer', string='Customer', ondelete='restrict')
    book_id = fields.Many2one('library.book', string='Books', ondelete='restrict')