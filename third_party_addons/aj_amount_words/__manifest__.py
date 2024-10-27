{
    'name': 'Amount in Words',
    'summary': """Total Amount in Word for Sales, and Purchase both in view
    and report.""",
    'version': '1.1',
    'category': 'Sales/Sales',
    'author': 'Arun',
    'depends': ['sale', 'purchase', ],
    'data': [
        'views/sale_view.xml',
        'views/purchase_view.xml',
        'report/report.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
    'external_dependencies': {
        'python': ['num2words'],
    }
}
