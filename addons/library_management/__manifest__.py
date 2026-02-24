{
    "name": "Library Management",
    "version": "1.0",
    "category": "Services/Library",
    "summary": "Library management system: Books and rent records management",
    "description": """
        This module provides core library management features:
        - Management of the book collection.
        - Real-time book availability tracking.
        - Renting process management for partners (customers).
        - Control over return dates and rental constraints.
    """,
    # 'base' is required because we utilize the 'res.partner' model and basic Odoo features
    "depends": ["base"],
    "data": [
        # Security access rules must be loaded first
        "security/ir.model.access.csv",
        # Actions and wizard views
        "views/wizard_views.xml",
        # Main model views
        "views/library_book_views.xml",
        "views/library_rent_views.xml",
        # Menu (usually loaded last)
        "views/menus.xml",
    ],
    "installable": True,  # Allows the module to be installed in the database
    "application": True,  # Marks the module as a standalone App in the Apps dashboard
    "license": "LGPL-3",
}
