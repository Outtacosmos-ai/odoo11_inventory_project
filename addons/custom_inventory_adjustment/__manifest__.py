{
    'name': 'Custom Inventory Adjustments',
    'version': '11.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Enhance inventory adjustments functionality',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['stock'],
    'data': [
        'security/inventory_security.xml',
        'security/ir.model.access.csv',
        'views/inventory_adjustment_views.xml',
        'data/inventory_adjustment_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
