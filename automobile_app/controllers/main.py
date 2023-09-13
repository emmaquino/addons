from odoo import http

class Vehicle(http.Controller):

    @http.route("/automobile/fleet")
    def list(self, **kwargs):
        vehicle = http.request.env["automobile.vehicle"]
        fleet = vehicle.search([])
        return http.request.render(
            "automobile_app.fleet_list_template",
            {"vehicle": fleet}
        )