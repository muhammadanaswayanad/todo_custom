{
    'name': 'Todo Custom',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Customizations for Todo module',
    'description': 'This module provides customizations for the Todo module.',
    'author': 'Your Name',
    'depends': ['base'],  # Ensure 'todo_custom' does not depend on 'todo_stage'
    'data': [
        // ...existing code...
    ],
    'installable': True,
    'application': False,
}
