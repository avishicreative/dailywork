# -*- coding: utf-8 -*-
# from odoo import http


# class Custom1(http.Controller):
#     @http.route('/custom1/custom1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom1/custom1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom1.listing', {
#             'root': '/custom1/custom1',
#             'objects': http.request.env['custom1.custom1'].search([]),
#         })

#     @http.route('/custom1/custom1/objects/<model("custom1.custom1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom1.object', {
#             'object': obj
#         })
