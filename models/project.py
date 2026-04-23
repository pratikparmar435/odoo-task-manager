from odoo import models,fields

class Project(models.Model):
    _name = 'task.project'
    _description = 'Project'

    name = fields.Char(string='project name',required=True)
    