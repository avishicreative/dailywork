# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom3(models.Model):
     _name = 'custom3.custom3'
     _description = 'custom3.custom3'
     _inherit = 'custom1.custom1'

     company=fields.Char()
     post=fields.Char()