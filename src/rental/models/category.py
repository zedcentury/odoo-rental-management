from odoo import models, fields, _


class Category(models.Model):
    _name = "rental.category"
    _description = "Category Model"

    name = fields.Char(string="Name", required=True, translate=True)
    active = fields.Boolean(default=True, string="Active")
    product_ids = fields.One2many("rental.product", "category_id", string="Products")

    def action_toggle(self):
        name = _("Mening ismim %s") % self.name
