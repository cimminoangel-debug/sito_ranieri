from django.urls import path
from . import views

urlpatterns = [
    # Pagine Principali del Portale
    path('', views.home, name='home'),
    path('discografia/', views.discografia, name='discografia'),
    path('concerti/tutti/', views.tutti_i_concerti, name='tutti_i_concerti'), # <-- Nuova riga
    
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
    path('biografia/', views.lista_biografia, name='lista_biografia'),
    path('biografia/<int:evento_id>/', views.dettaglio_biografia, name='dettaglio_biografia'),
    path('canzoni/', views.CanzoneListView.as_view(), name='canzone_list'),
    path('canzoni/nuova/', views.CanzoneCreateView.as_view(), name='canzone_create'),
    path('canzoni/<int:pk>/modifica/', views.CanzoneUpdateView.as_view(), name='canzone_update'),
    path('canzoni/<int:pk>/elimina/', views.CanzoneDeleteView.as_view(), name='canzone_delete'), 
    path('concerti/', views.ConcertoListView.as_view(), name='concerto_list'),
    path('concerti/nuovo/', views.ConcertoCreateView.as_view(), name='concerto_create'),
    path('concerti/<int:pk>/modifica/', views.ConcertoUpdateView.as_view(), name='concerto_update'),
    path('concerti/<int:pk>/elimina/', views.ConcertoDeleteView.as_view(), name='concerto_delete'),
    path('biografie/', views.BiografiaListView.as_view(), name='biografia_list'),
    path('biografie/nuova/', views.BiografiaCreateView.as_view(), name='biografia_create'),
    path('biografie/<int:pk>/modifica/', views.BiografiaUpdateView.as_view(), name='biografia_update'),
    path('biografie/<int:pk>/elimina/', views.BiografiaDeleteView.as_view(), name='biografia_delete'),
]
