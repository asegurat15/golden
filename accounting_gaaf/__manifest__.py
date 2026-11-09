# -*- coding: utf-8 -*-
{
    'name': "Gaaf Custom Account",
    'summary': "Personalizaciones y mejoras específicas para Ag Supply",
    'description': """
Este módulo incluye un conjunto de personalizaciones y mejoras desarrolladas específicamente para la empresa Ag Supply.
------------
Las funcionalidades incluyen:
    """,
    'author': "Kuai-mare Carrasquero",
    'version': '0.1',
    'depends': ['base', 'account', 'l10n_do_accounting'],
    'data': [
        'views/account_account_inherit_views.xml',
        'views/report_invoice.xml',
        'views/account_move_views.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
