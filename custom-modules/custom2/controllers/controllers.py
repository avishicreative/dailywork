# -*- coding: utf-8 -*-
# from odoo import http


# class Custom2(http.Controller):
#     @http.route('/custom2/custom2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom2/custom2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom2.listing', {
#             'root': '/custom2/custom2',
#             'objects': http.request.env['custom2.custom2'].search([]),
#         })

#     @http.route('/custom2/custom2/objects/<model("custom2.custom2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom2.object', {
#             'object': obj
#         })
