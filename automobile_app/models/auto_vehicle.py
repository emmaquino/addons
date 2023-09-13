from odoo import fields, models

class Vehicle(models.Model):
    _name = "automobile.vehicle"
    _description = "Vehicle"
    vin = fields.Char("VIN", required=True)
    model = fields.Char("Model")
    make = fields.Char("Make")
    year = fields.Integer("Year")
    mileage = fields.Integer("Mileage")
    image = fields.Binary("Image")
    added_by = fields.Many2one("res.partner", string="Added by")
    date_added = fields.Date()