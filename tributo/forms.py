from django import forms
from .models import Canzone
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
