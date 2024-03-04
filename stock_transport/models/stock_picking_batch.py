from odoo import api, fields, models


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"
    _description = "Batch Transfer"

    dock_id = fields.Many2one("stock.transport.dock", string="Dock")
    vehicle = fields.Many2one("fleet.vehicle", required=False, string="Vehicle")
    vehicle_category = fields.Many2one(
        "fleet.vehicle.model.category", string="Vehicle Category"
    )
    max_weight = fields.Float(related="vehicle_category.max_weight")
    max_volume = fields.Float(related="vehicle_category.max_volume")
    weight = fields.Float(compute="_compute_weight", store=True)
    volume = fields.Float(compute="_compute_volume", store=True)
    transfers = fields.Integer(
        compute="_compute_transfers", store=True, string="No of Transfers"
    )
    detailed_operations = fields.Integer(
        compute="_compute_detailed_operations", store=True, string="No of Lines"
    )

    @api.depends("max_weight", "picking_ids")
    def _compute_weight(self):
        for rec in self:
            total = 0
            for picking_line in rec.picking_ids:
                total += picking_line.picking_weight

        if rec.max_weight > 0:
            rec.weight = 100 * (total / rec.max_weight)
        else:
            rec.weight = 0

    @api.depends("max_volume", "picking_ids")
    def _compute_volume(self):
        for rec in self:
            total = 0
            for picking_line in rec.picking_ids:
                total += picking_line.picking_volume
        if rec.max_volume > 0:
            rec.volume = 100 * (total / rec.max_volume)
        else:
            rec.volume = 0

    # To count no of transfers and then showing it in graph view of batch transfers
    @api.depends("picking_ids")
    def _compute_transfers(self):
        for rec in self:
            rec.transfers = 0
            for picking in rec.picking_ids:
                rec.transfers = rec.transfers + 1

    # To count no of detailed operation lines and showing it in graph view of batch transfers
    @api.depends("move_line_ids")
    def _compute_detailed_operations(self):
        for rec in self:
            rec.detailed_operations = 0
            for line in rec.move_line_ids:
                rec.detailed_operations = rec.detailed_operations + 1

    @api.depends("weight", "volume", "name")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name}: ({rec.weight}kg, {rec.volume}m3)"
        return True
