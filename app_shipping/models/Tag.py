from odoo import models , fields , api

class Tag(models.Model):
    _name = 'order_tag'

    name = fields.Char(required=True)
    color = fields.Integer()  # Optional: to assign a color to the tag