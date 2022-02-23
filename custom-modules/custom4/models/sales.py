from odoo import models, fields, api


class saleOrder(models.Model):
    _inherit = 'sale.order'
    #_description = 'custom4.custom4'

    company = fields.Char()
    post = fields.Char()
