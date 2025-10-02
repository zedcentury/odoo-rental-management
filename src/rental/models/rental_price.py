from odoo import models, fields, api


class RentalPrice(models.Model):
    _name = "rental.price"
    _description = "Rental Price"

    product_id = fields.Many2one("rental.product", required=True, ondelete="cascade")
    interval_number = fields.Integer(
        string="Interval Number",
        required=True,
    )
    interval_type = fields.Selection([
        ("hour", "Hour"),
        ("day", "Day"),
        ("week", "Week"),
        ("month", "Month"),
        ("year", "Year"),
    ], default="hour", required=True)

    hour = fields.Integer(compute="_compute_hour", store=True)

    price = fields.Float("Price", required=True)

    @api.depends("interval_number", "interval_type")
    def _compute_hour(self):
        for record in self:
            if record.interval_type == "hour":
                hours = 1
            elif record.interval_type == "day":
                hours = 24
            elif record.interval_type == "week":
                hours = 168
            elif record.interval_type == "month":
                hours = 24 * 30
            else:
                hours = 24 * 365

            record.hour = record.interval_number * hours

    """
    1 hour - 5.000
    1 day - 7.000
    
    3 day
    
    1 week - 10.000
    1 month - 20.000
    """

    @api.model
    def get_min_rental_price(self, product_id, hours):
        rps = self.env["rental.price"].search([("product_id", "=", product_id), ("hour", "<=", hours)],
                                              order="hour asc")

        if not rps:
            return None

        return rps[-1]

    @api.model
    def get_max_rental_price(self, product_id, hours):
        rps = self.env["rental.price"].search([("product_id", "=", product_id), ("hour", ">=", hours)],
                                              order="hour asc")

        if not rps:
            return None

        return rps[0]

    @api.model
    def get_result_price(self, product_id, hours):
        min_rental_price = self.get_min_rental_price(product_id, hours)
        max_rental_price = self.get_max_rental_price(product_id, hours)

        price_by_min = min_rental_price.price * (hours / min_rental_price.hour)
        price_by_max = max_rental_price.price

        return min(price_by_min, price_by_max)

