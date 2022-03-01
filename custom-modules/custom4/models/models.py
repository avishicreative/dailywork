# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom4(models.Model):
      _name = 'custom4.custom4'
      _description = 'custom4.custom4'



      user_id=fields.Many2one('custom1.custom1',string="customer")
      flight_id1=fields.Many2one('custom3.custom3',string="flight")
      #total=fields.Many2one(string='price',related="flight_id1.price")
      fly_to=fields.Many2one(string='destination',related="flight_id1.destination")
      fly_from = fields.Many2one(string='arrival', related="flight_id1.arrival")