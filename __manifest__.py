# Copyright 2024 Munin
{
    "name": "Force Width css",
    "version": "17.0.1.0.0",
    "author": "Munin",
    "category": "web",
    "license": "AGPL-3",
    "depends": [
        "base", "web", "sale"
    ],
    "data": [
        "views/sale_order_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "css_force_width/static/src/css/*",
            ],
    },
    "installable": True,
}
