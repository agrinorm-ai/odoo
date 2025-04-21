from odoo import models, fields

class AgBatch(models.Model):
    _name = 'ag.batch'
    _description = 'Batch'
    
    parent_id = fields.Many2one('ag.batch', string='Parent ID', ondelete='restrict') 
    child_ids = fields.One2many('ag.batch', 'parent_id', string='Child IDs')
