
from odoo import models, fields


class MaterialCategory(models.Model):
    _name = 'batchflow.material.category'
    _description = 'Material Category'
    _rec_name = 'name'

    name = fields.Char(
        string='Category Name',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )