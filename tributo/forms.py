from django import forms
from django.forms import inlineformset_factory
from .models import Canzone, Concerto, Biografia, Foto_Gallery, Video_Gallery
from django_ckeditor_5.widgets import CKEditor5Widget # 1. Importa il widget

class CanzoneForm(forms.ModelForm):
    class Meta:
        model = Canzone
        fields = ['titolo', 'anno_uscita', 'testo', 'copertina', 'prezzo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 2. Assegna il widget di CKEditor 5 al campo testo
        # Usa config_name='default' (o il nome della configurazione definita nel tuo settings.py)
        self.fields['testo'].widget = CKEditor5Widget(
            attrs={"class": "django_ckeditor_5"}, 
            config_name="default"
        )
        # Se usi Crispy Forms, è importante forzare la classe corretta
        self.fields['testo'].required = False


class ConcertoForm(forms.ModelForm):
    class Meta:
        model = Concerto
        fields = ['luogo', 'citta', 'data', 'locandina', 'prezzo']
        widgets = {
            # Questo widget mostra il calendario nativo del browser
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Forza Django a interpretare correttamente la data nel form
        self.fields['data'].input_formats = ['%Y-%m-%d']

class BiografiaForm(forms.ModelForm):
    class Meta:
        model = Biografia
        fields = ['titolo_evento', 'data_evento', 'luogo', 'descrizione']
        widgets = {
            'data_evento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sincronizza il formato data
        self.fields['data_evento'].input_formats = ['%Y-%m-%d']


# FORMSET PER LE FOTO (Fino a 3 campi pronti da compilare)
FotoGalleryFormSet = inlineformset_factory(
    Biografia, 
    Foto_Gallery,
    fields=['titolo_foto', 'immagine'],
    extra=0,             # <--- CAMBIATO A 0: nessuna riga vuota iniziale
    can_delete=True,     
    widgets={
        'titolo_foto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Didascalia della foto'}),
        'immagine': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
)

# FORMSET PER I VIDEO (extra=0)
VideoGalleryFormSet = inlineformset_factory(
    Biografia, 
    Video_Gallery,
    fields=['titolo_video', 'file_video'],
    extra=0,             # <--- CAMBIATO A 0: nessuna riga vuota iniziale
    can_delete=True,     
    widgets={
        'titolo_video': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titolo del video'}),
        'file_video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
)