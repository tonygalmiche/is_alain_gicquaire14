# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 14 pour Alain Gicquaire',
    'version'  : '14.0.0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 14 pour Alain Gicquaire
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'account',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/account_move_views.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
    'application': True,
}
