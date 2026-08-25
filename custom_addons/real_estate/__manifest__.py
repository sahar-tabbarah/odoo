{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real Estate Management',
    'description': 'A real estate management module for Odoo.',
    'author': 'Sahar Tabbarah',
    'category': 'Real Estate',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}