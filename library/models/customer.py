# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):
    _description = 'Customer'
    _name = 'library.customer'
    
    name = fields.Char(string='Customer Name', required=True)
    date_of_birth = fields.Date(required=True)
    address = fields.Char(required=True)
    postcode = fields.Char(required=True)
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')