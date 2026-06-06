from django.contrib import admin
from django.utils.html import format_html # <-- Fondamentale per inserire codice HTML sicuro
from .models import Canzone, Concerto, Biografia, Partecipante, VideoSpettacolo

@admin.register(Canzone)
class CanzoneAdmin(admin.ModelAdmin):
    # Mostra la miniatura nella tabella riassuntiva insieme a titolo e anno
    list_display = ('anteprima_copertina', 'titolo', 'anno_uscita', 'prezzo')
    # Rende cliccabile anche la miniatura per entrare nella modifica
    list_display_links = ('anteprima_copertina', 'titolo')

    # Funzione interna per generare il tag HTML dell'immagine
    def anteprima_copertina(self, obj):
        if obj.copertina:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px; border: 1px solid #ddd;" />', obj.copertina.url)
        return "Nessuna foto"
    
    # Assegna il titolo alla colonna nell'admin
    anteprima_copertina.short_description = 'Copertina'


@admin.register(Concerto)
class ConcertoAdmin(admin.ModelAdmin):
    list_display = ('anteprima_locandina', 'luogo', 'citta', 'data', 'prezzo')
    list_display_links = ('anteprima_locandina', 'luogo')

    def anteprima_locandina(self, obj):
        if obj.locandina:
            return format_html('<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 4px; border: 1px solid #ddd;" />', obj.locandina.url)
        return "No Locandina"
    
    anteprima_locandina.short_description = 'Locandina'


@admin.register(Biografia)
class BiografiaAdmin(admin.ModelAdmin):
    list_display = ('anteprima_foto', 'titolo_sezione', 'anno_inizio_carriera')
    list_display_links = ('anteprima_foto', 'titolo_sezione')

    def anteprima_foto(self, obj):
        if obj.foto_artista:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%; border: 1px solid #ddd;" />', obj.foto_artista.url)
        return "No Foto"
    
    anteprima_foto.short_description = 'Foto Artista'


# Lasciamo il modello Partecipante con la registrazione standard
admin.site.register(Partecipante)

@admin.register(VideoSpettacolo)
class VideoSpettacoloAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'data_aggiunta')
    search_fields = ('titolo',)
