# -*- coding: utf-8 -*-
# from odoo import http


# class Ofm(http.Controller):
#     @http.route('/ofm/ofm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ofm/ofm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ofm.listing', {
#             'root': '/ofm/ofm',
#             'objects': http.request.env['ofm.ofm'].search([]),
#         })

#     @http.route('/ofm/ofm/objects/<model("ofm.ofm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ofm.object', {
#             'object': obj
#         })
