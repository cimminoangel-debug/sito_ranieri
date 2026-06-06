from django.urls import path
from . import views

urlpatterns = [
    # Pagine Principali del Portale
    path('', views.home, name='home'),
    path('discografia/', views.discografia, name='discografia'),
    path('concerti/tutti/', views.tutti_i_concerti, name='tutti_i_concerti'), # <-- Nuova riga
    path('biografia/', views.biografia, name='biografia'),
    
    # Flusso Acquisto Brani Musicali (Stripe)
    path('ordine/<int:canzone_id>/riepilogo/', views.ordine_riepilogo, name='ordine_riepilogo'),
    path('ordine/canzone/pagamento/successo/', views.canzone_pagamento_successo, name='canzone_pagamento_successo'),
    
    # Flusso Biglietti Concerti (Stripe)
    path('concerto/<int:concerto_id>/riepilogo/', views.concerto_riepilogo, name='concerto_riepilogo'),
    path('concerto/pagamento/successo/', views.concerto_pagamento_successo, name='pagamento_successo'),
    
    # Controllo Accessi e Registro Biglietteria
    path('gestione/valida/<str:codice_biglietto>/', views.valida_biglietto, name='valida_biglietto'),
    path('gestione/partecipanti/', views.lista_partecipanti, name='lista_partecipanti'),
    path('gestione/partecipanti/pdf/<int:partecipante_id>/', views.vedi_pdf_biglietto, name='vedi_pdf_biglietto'),
    path('gestione/partecipanti/reinvia/<int:partecipante_id>/', views.reinvia_biglietto, name='reinvia_biglietto'),
    path('gestione/partecipanti/esporta/excel/', views.esporta_excel_partecipanti, name='esporta_excel_partecipanti'),
    # Nuova rotta per la schermata della fotocamera del controllore
    path('gestione/scanner/', views.dashboard_scanner, name='dashboard_scanner'),
    
]
