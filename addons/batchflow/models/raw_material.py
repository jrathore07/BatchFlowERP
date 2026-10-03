from odoo import models, fields


class RawMaterial(models.Model):
    _name = 'batchflow.raw.material'
    _description = 'Raw Material'

    name = fields.Char(
        string='Material Name',
        required=True
    )

    code = fields.Char(
        string='Material Code',
        required=True
    )

    category_id = fields.Many2one(
    'batchflow.material.category',
    string='Category',
    required=True
)

    unit = fields.Char(
        string='Unit',
        default='kg'
    )

    quantity = fields.Float(
        string='Quantity',
        default=0.0
    )

    cost = fields.Float(
        string='Cost',
        default=0.0
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    _unique_material_code = models.Constraint(
        'UNIQUE(code)',
        'Material Code must be unique.'
    )