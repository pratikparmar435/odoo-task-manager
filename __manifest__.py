{
    'name': 'Task Manager',
    'version': '1.0',
    'summary': 'Simple Task Manager Module built with Odoo ORM',
    'depends': ['base'],
    'application': True,  
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}