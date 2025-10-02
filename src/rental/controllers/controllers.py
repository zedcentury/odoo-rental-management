# -*- coding: utf-8 -*-
# from odoo import http


# class Rental(http.Controller):
#     @http.route('/rental/rental', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rental/rental/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rental.listing', {
#             'root': '/rental/rental',
#             'objects': http.request.env['rental.rental'].search([]),
#         })

#     @http.route('/rental/rental/objects/<model("rental.rental"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rental.object', {
#             'object': obj
#         })

