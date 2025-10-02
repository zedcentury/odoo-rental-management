from odoo import models, fields, api


class RentalOrder(models.Model):
    _name = "rental.order"
    _description = "Rental Order"

    name = fields.Char(string="Name", required=True, default="New")
    product_id = fields.Many2one("rental.product", required=True)
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    total_price = fields.Float(string="Total Price", required=True, compute="_compute_total_price")

    def _compute_total_price(self):
        for record in self:
            hours = (record.end_date - record.start_date).days * 24
            total_price = self.env["rental.price"].get_result_price(product_id=record.product_id.id, hours=hours)
            record.total_price = total_price

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('rental.order')  # RO002

        return super().create(vals_list)
