{
    'name': 'Todo Stage',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Module to set stages for Todo module',
    'description': 'This module sets fixed stages for the Todo module.',
    'author': 'Your Name',
    'depends': ['base', 'todo_custom'],
    'data': [
        'data/todo_stage_data.xml',
        'views/todo_stage_views.xml',
    ],
    'installable': True,
    'application': False,
}
