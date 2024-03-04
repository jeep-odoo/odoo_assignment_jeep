from odoo import fields,models

class StockTransportDock(models.Model):
    _name = "stock.transport.dock"
    _description = "Dock Model"
    
    name = fields.Char()
