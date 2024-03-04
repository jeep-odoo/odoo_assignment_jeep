from odoo import api, fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    picking_weight = fields.Float(compute="_compute_picking_weight", string="Weight")
    picking_volume = fields.Float(compute="_compute_picking_volume", string="Volume")

    @api.depends("move_line_ids")
    def _compute_picking_weight(self):
        self.picking_weight=0
        for rec in self:
            for move_line in rec.move_line_ids:
                rec.picking_weight += move_line.quantity * move_line.product_id.weight
        

    @api.depends("move_line_ids")
    def _compute_picking_volume(self):
        self.picking_volume=0
        for rec in self:
            for move_line in rec.move_line_ids:
                rec.picking_volume += move_line.quantity * move_line.product_id.volume
