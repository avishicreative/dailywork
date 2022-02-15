# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom1(models.Model):
     _name = 'custom1.custom1'
     _description = 'custom1.custom1'

     fname = fields.Char()
     mobile = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     address = fields.Text()
     city = fields.Char()
     gender=fields.Selection([('girl','female'),('boy','male')])
     image=fields.Binary()
     choice=fields.Selection([('yes','true'),('no','false')])
     @api.depends('mobile')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.mobile) / 100
