# -*- coding: utf-8 -*-
# from odoo import http


# class AutomobileApp(http.Controller):
#     @http.route('/automobile_app/automobile_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/automobile_app/automobile_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('automobile_app.listing', {
#             'root': '/automobile_app/automobile_app',
#             'objects': http.request.env['automobile_app.automobile_app'].search([]),
#         })

#     @http.route('/automobile_app/automobile_app/objects/<model("automobile_app.automobile_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automobile_app.object', {
#             'object': obj
#         })
