# -*- coding: utf-8 -*-
{
    "name": "ofm",
    "summary": """
        Organización de Festivales de Música""",
    "description": """
        Módulo para la gestión de Festivales de Música (Proyecto SGE 2º DAM).
        
        Funcionalidades principales:
        - Gestión de Participantes: Registro de Artistas (con caché y rider) y Staff (seguridad, técnicos).
        - Logística: Gestión de Escenarios y Patrocinadores.
        - Eventos: Planificación de Actuaciones (horarios y asignación de escenarios).
        - Ventas: Control de Entradas vendidas.
    """,
    "author": "Víctor Manuel Freitas Moray, Adrián Márquez Bellido, Jesús Valdivia García",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        'views/participante_view.xml',
        "views/actuacion_views.xml",
        "views/entrada_views.xml",
        "views/artista_view.xml",
        "views/staff_view.xml",
        "views/escenario_view.xml",
        "views/patrocinador_view.xml",
        "views/menu_view.xml",
        "reports/escenario_report.xml",
        "reports/patrocinador_report.xml",
        "reports/reports.xml",
        "reports/artista_report.xml",
        "reports/staff_report.xml",
        "reports/entrada_report.xml",
        "reports/actuacion_report.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
    # Esto hace que sea una aplicación instalable
    #'installable': True,
}
