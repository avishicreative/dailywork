# -*- coding: utf-8 -*-
# from odoo import http


# class custom4(http.Controller):
#     @http.route('/custom4/custom4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom4/custom4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom4.listing', {
#             'root': '/custom4/custom4',
#             'objects': http.request.env['custom4.custom4'].search([]),
#         })

#     @http.route('/custom4/custom4/objects/<model("custom4.custom4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom4.object', {
#             'object': obj
#         })
