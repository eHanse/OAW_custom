# -*- coding: utf-8 -*-
from odoo import http

# class ./chr123Reports(http.Controller):
#     @http.route('/./chr123_reports/./chr123_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./chr123_reports/./chr123_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./chr123_reports.listing', {
#             'root': '/./chr123_reports/./chr123_reports',
#             'objects': http.request.env['./chr123_reports../chr123_reports'].search([]),
#         })

#     @http.route('/./chr123_reports/./chr123_reports/objects/<model("./chr123_reports../chr123_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./chr123_reports.object', {
#             'object': obj
#         })