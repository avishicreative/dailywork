# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wiz(models.Model):
     _name = 'wiz.wiz'
     #_description = 'wiz'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100

     def wiz_print(self):
         print("avish")
