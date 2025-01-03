from odoo import models, fields

class TodoStage(models.Model):
    _name = 'todo.stage'
    _description = 'Todo Stage'

    name = fields.Char(string='Stage Name', required=True)
    personal_stage_type_id = fields.Selection([
        ('a_category', 'A Category'),
        ('b_category', 'B Category'),
        ('c_category', 'C Category'),
        ('d_category', 'D Category'),
    ], string='Personal Stage Type', required=True)
