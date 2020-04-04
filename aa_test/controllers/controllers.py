# -*- coding: utf-8 -*-
# from odoo import http


# class AaTest(http.Controller):
#     @http.route('/aa_test/aa_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aa_test/aa_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aa_test.listing', {
#             'root': '/aa_test/aa_test',
#             'objects': http.request.env['aa_test.aa_test'].search([]),
#         })

#     @http.route('/aa_test/aa_test/objects/<model("aa_test.aa_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aa_test.object', {
#             'object': obj
#         })
