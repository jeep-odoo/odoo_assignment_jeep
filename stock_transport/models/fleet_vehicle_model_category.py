from odoo import fields, models, api


class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight (Kg)")
    max_volume = fields.Float(string="Max Volume (m3)")

    _sql_constraints = [
        (
            "check_weight_volume",
            "CHECK(max_weight > 0 AND max_volume > 0)",
            "The maximum weight and volume must be greater than zero",
        )
    ]

    @api.depends("max_weight", "max_volume", "name")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} ({rec.max_weight}kg, {rec.max_volume}m3)"
        return True
