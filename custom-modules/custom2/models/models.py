# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom2(models.Model):
    _name = 'custom2.custom2'
    #_inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'custom2.custom2'
    _rec_name = "city"


    air_name = fields.Char()
    city = fields.Char()
    type = fields.Char()

