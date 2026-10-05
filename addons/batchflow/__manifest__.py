{
    'name': 'BatchFlow ERP',
    'version': '1.0.0',
    'category': 'Manufacturing',
    'summary': 'Process manufacturing and batch management ERP',
    'description': """
        BatchFlow ERP
        =============

        ERP system for process manufacturing businesses.

        Modules:
        - Product Management
        - Raw Materials
        - Formulation
        - Manufacturing Batches
        - Quality Inspection
        - Inventory
    """,
    'author': 'Jaydeep Rathore',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [ 'security/security.xml',
              'security/ir.model.access.csv',
             'views/raw_material_views.xml',
             'views/material_category_views.xml',],
    'installable': True,
    'application': True,
}