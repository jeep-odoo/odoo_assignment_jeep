{
    "name": "Stock Transport",
    "version": "1.0",
    "depends": ["stock_picking_batch", "fleet"],
    "author": "jeep-odoo",
    "data": [
        "security/ir.model.access.csv",
        "views/fleet_vehicle_model_category_views.xml",
        "views/inherited_stock_picking_batch_views.xml",
        "views/inherited_stock_picking_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
