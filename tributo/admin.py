from django.contrib import admin
from django.utils.html import format_html # <-- Fondamentale per inserire codice HTML sicuro
from .models import Canzone, Concerto, Biografia, Partecipante, Video_Gallery, Foto_Gallery, TuoModello

class VideoInline(admin.TabularInline):
    model = Video_Gallery
    extra = 1

class FotoInline(admin.TabularInline):
    model = Foto_Gallery
    extra = 1

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
    # Mostra l'anteprima della prima foto, la data, il titolo dell'evento e il luogo
    list_display = ('anteprima_foto', 'data_evento', 'titolo_evento', 'luogo')
    list_display_links = ('anteprima_foto', 'titolo_evento')
    inlines = [VideoInline, FotoInline]

    def anteprima_foto(self, obj):
        # Prende la prima foto collegata a questo specifico evento, se esiste
        prima_foto = obj.fotos.first()
        if prima_foto and prima_foto.immagine:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px; border: 1px solid #ddd;" />', prima_foto.immagine.url)
        return format_html('<span style="color: #999; font-style: italic;">No Foto</span>')
    
    anteprima_foto.short_description = 'Anteprima Galleria'


# Lasciamo il modello Partecipante con la registrazione standard
admin.site.register(Partecipante)

@admin.register(TuoModello)
class TuoModelloAdmin(admin.ModelAdmin):
    list_display = ('id',)# o altri campi che vuoi mostrare nella tabella
