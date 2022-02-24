# -*- coding: utf-8 -*-

from odoo import models, fields, api


class c3wiz(models.TransientModel):
     _name = 'c3wiz.c3wiz'
     _description = 'c3.wiz'
     

     fname=fields.Char()
     lname=fields.Char()
     
     def pname(self):
     	print("fname and lname saved")
