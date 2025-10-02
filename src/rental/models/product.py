from odoo import models, fields


class Product(models.Model):
    _name = "rental.product"
    _inherit = "image.mixin"
    _description = "Product"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
