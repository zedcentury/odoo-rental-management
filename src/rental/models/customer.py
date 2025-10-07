from odoo import models, fields


class Customer(models.Model):
    _name = "rental.customer"
    _description = "Customer"

    name = fields.Char(string="Name", required=True)
    order_ids = fields.One2many("rental.order", "customer_id", string="Orders")
