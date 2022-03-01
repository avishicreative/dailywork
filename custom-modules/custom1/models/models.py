# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom1(models.Model):
     _name = 'custom1.custom1'
     _description = 'custom1.custom1'
     _rec_name = "fname"

     fname = fields.Char()
     lname=fields.Char()
     mobile = fields.Integer()

     address = fields.Text()
     city = fields.Char()
     gender=fields.Selection([('girl','female'),('boy','male')])
     image=fields.Binary()
     choice=fields.Selection([('yes','true'),('no','false')])
     status=fields.Selection([('draft','Draft'),
                              ('inprocess','Processing'),('done','Done'),('cancel','Cancel')],string='status',default='draft')
     skills=fields.Many2one('res.partner',string='Skills')
     


     def action_confirm(self):
          for rec in self:
               male=self.env['custom1.custom1'].search([('gender', '=', 'boy')])
               print(male)