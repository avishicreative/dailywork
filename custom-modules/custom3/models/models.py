# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom3(models.Model):
     _name = 'custom3.custom3'
     _description = 'custom3.custom3'
     #_inherit = 'custom1.custom1'
     _rec_name = "flightid"

     flightid=fields.Integer()
     departure_time=fields.Datetime()
     arrival_time = fields.Datetime()
     departure = fields.Many2one('custom2.custom2',string="departure")
     arrival=fields.Many2one('custom2.custom2',string="arrival")
     #company=fields.Char()
     #post=fields.Char()
     price=fields.Integer()


     def name1(self):
          return {
               'name': ('smartbutton'),
               'domain': [],
               'view_type': 'form',
               'res_model': 'custom1.custom1',
               'view_id': False,
               'view_mode': 'tree,form',
               'type': 'ir.actions.act_window'
          }

     def name2(self):
          return {
               'name': ('smartbutton'),
               'domain': [],
               'view_type': 'form',
               'res_model': 'custom2.custom2',
               'view_id': False,
               'view_mode': 'tree,form',
               'type': 'ir.actions.act_window'
          }

     def name3(self):
         return {
                    'name': ('smartbutton'),
                    'domain': [],
                    'view_type': 'form',
                    'res_model': 'custom3.custom3',
                    'view_id': False,
                    'view_mode': 'tree,form',
                    'type': 'ir.actions.act_window'
               }

     def name4(self):
        return {
                         'name': ('smartbutton'),
                         'domain': [],
                         'view_type': 'form',
                         'res_model': 'custom4.custom4',
                         'view_id': False,
                         'view_mode': 'tree,form',
                         'type': 'ir.actions.act_window'
                    }
