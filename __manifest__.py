{
    'name':'Chequeador',
    'author': "Desoft",
    'depends':[
        'base',
        'fleet',
    ],
    'data':[
        'security/ir.model.access.csv',
        'data/chequeador_menu.xml',
        'views/chequeador_camion_modelo_view.xml',
        'views/chequeador_camion.xml',
        'views/chequeador_destino_views.xml',
        'views/chequeador_origen_views.xml',
    ],
    'installable': True,
    'application': True
}