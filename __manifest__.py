{
    'name': 'Student Management',
    'version': '19.0.1.0.0',
    'summary': 'Manage student records with validation rules (TDD project)',
    'description': """
Student Management System
==========================
A simple Odoo module to manage student records, built using
Test-Driven Development (TDD).
""",
    'category': 'Education',
    'author': 'Ameer',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/student_security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],

    'installable': True,
    'application': True,
}
