# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom4(models.Model):
      _name = 'custom4.custom4'
      _description = 'custom4.custom4'


      name=fields.Char()
      age=fields.Integer()