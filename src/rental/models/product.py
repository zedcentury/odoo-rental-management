from odoo import models, fields


class Product(models.Model):
    _name = "rental.product"
    _description = "Product"

    name = fields.Char(string="Name", required=True)
