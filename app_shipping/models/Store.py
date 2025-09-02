from odoo import models , fields , api

class StoreDone(models.Model):
    _name = 'store_done'

    name = fields.Char(required=True)
    location = fields.Text(required=True)
    order_ids = fields.One2many('order', 'store_id', string="Orders")
