# -*- coding: utf-8 -*-
from openerp import http

# class MyFieldSupRefIntoTreeView(http.Controller):
#     @http.route('/my_field_sup_ref_into_tree_view/my_field_sup_ref_into_tree_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_field_sup_ref_into_tree_view/my_field_sup_ref_into_tree_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_field_sup_ref_into_tree_view.listing', {
#             'root': '/my_field_sup_ref_into_tree_view/my_field_sup_ref_into_tree_view',
#             'objects': http.request.env['my_field_sup_ref_into_tree_view.my_field_sup_ref_into_tree_view'].search([]),
#         })

#     @http.route('/my_field_sup_ref_into_tree_view/my_field_sup_ref_into_tree_view/objects/<models("my_field_sup_ref_into_tree_view.my_field_sup_ref_into_tree_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_field_sup_ref_into_tree_view.object', {
#             'object': obj
#         })