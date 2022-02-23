# -*- coding: utf-8 -*-
# from odoo import http


# class Custom3(http.Controller):
#     @http.route('/custom3/custom3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom3/custom3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom3.listing', {
#             'root': '/custom3/custom3',
#             'objects': http.request.env['custom3.custom3'].search([]),
#         })

#     @http.route('/custom3/custom3/objects/<model("custom3.custom3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom3.object', {
#             'object': obj
#         })
