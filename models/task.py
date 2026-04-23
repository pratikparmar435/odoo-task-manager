from odoo import models, fields, api
from datetime import date

class Task(models.Model):
    _name = 'task.manager'
    _description = "Task Manager"

    name = fields.Char(string='Task Name',required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done')
    ], default='pending')
    deadline = fields.Date(string='Deadline',default=fields.Date.today)
    project_id = fields.Many2one('task.project',string='Project')
    is_overdue = fields.Boolean(string="Is Overdue",compute='_compute_is_overdue')

    @api.depends('deadline')
    def _compute_is_overdue(self):
        for task in self:
            if task.deadline:
                task.is_overdue = task.deadline < date.today()
            else:
                task.is_overdue = False
