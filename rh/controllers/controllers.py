# -*- coding: utf-8 -*-
# from odoo import http


# class Rh(http.Controller):
#     @http.route('/rh/rh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rh/rh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rh.listing', {
#             'root': '/rh/rh',
#             'objects': http.request.env['rh.rh'].search([]),
#         })

#     @http.route('/rh/rh/objects/<model("rh.rh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rh.object', {
#             'object': obj
#         })
