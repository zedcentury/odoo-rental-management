from odoo import models, fields


class Product(models.Model):
    _name = "rental.product"
    _inherit = ["image.mixin", "mail.thread"]
    _description = "Product"

    category_id = fields.Many2one("rental.category", string="Category")
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    broken = fields.Boolean(string="Broken", default=False, tracking=True)

    def action_broken_toggle(self):
        # admin_user = self.env["res.users"].sudo().search([("login", "=", "admin")], limit=1)
        admin_user = self.env.ref("base.user_admin")
        self.with_user(user=admin_user).write({"broken": not self.broken})

        # self.sudo().write({"broken": not self.broken})
