from odoo import models , fields , api

class order (models.Model):
    _name = 'order'


    name = fields.Text(required=True)
    sender_name = fields.Text(required=True)
    recipient_name = fields.Text(required=True)
    tracking_number = fields.Text(required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], default='draft' , required=True)
    address = fields.Text(required=True)
    city = fields.Text()
    state = fields.Text()
    zip_code = fields.Text()
    country = fields.Text()
    quantity = fields.Integer(required=True )
    store_id = fields.Many2one('store_done', string="Store", required=True)
    tag_ids = fields.Many2many('order_tag', string="Tags")

    _sql_constraints = [
        ('tracking_number_uniq', 'unique(tracking_number)', 'The tracking number must be unique!')
    ]

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")


    def action_mark_as_draft(self):
        for record in self:
            record.status = 'draft'

    def action_mark_as_shipped(self):
        for record in self:
            record.status = 'shipped'

    def action_mark_as_delivered(self):
        for record in self:
            record.status = 'delivered'
    
    def action_mark_as_cancel(self):
        for record in self:
            record.status = 'cancelled'
    # @api.model_create_multi
    # def create(self, vals_list):
    #     # Custom logic before creating records
    #     return super(order, self).create(vals_list)
    
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     return super()._search(domain, offset, limit, order, access_rights_uid)
    
    # def write(self, vals):
    #     return super(order, self).write(vals)
    
    # def unlink(self):
    #     return super(order, self).unlink()
