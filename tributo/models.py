from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class TuoModello(models.Model):
    # Richiama la configurazione 'default' definita in settings.py
    contenuto = CKEditor5Field('Contenuto', config_name='default')

class Canzone(models.Model):
    titolo = models.CharField(max_length=200)
    anno_uscita = models.IntegerField()
    testo = models.TextField(blank=True, null=True)
    # I file verranno salvati in media-serve/copertine/
    copertina = models.ImageField(upload_to='copertine/', blank=True, null=True)
    prezzo = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titolo

class Concerto(models.Model):
    luogo = models.CharField(max_length=200)
    citta = models.CharField(max_length=100)
    # Cambiato in DateField per la gestione cronologica reale
    data = models.DateField() 
    locandina = models.ImageField(upload_to='locandine/', blank=True, null=True)
    prezzo = models.DecimalField(max_digits=6, decimal_places=2, default=25.00)

    def __str__(self):
        return f"{self.luogo} ({self.citta}) - {self.data.strftime('%d/%m/%Y')}"
    # def __str__(self):
    #     # Se la data è presente, la formatta; altrimenti scrive "Data non definita"
    #     data_formattata = self.data.strftime('%d/%m/%Y') if self.data else "Data non definita"
    #     return f"{self.titolo} ({data_formattata})"

class Biografia(models.Model):
    """
    Rappresenta l'evento principale o la tappa della carriera (es. Concerto a Sanremo).
    """
    titolo_evento = models.CharField(max_length=200, verbose_name="Titolo Evento/Concerto")
    data_evento = models.DateField(verbose_name="Data dell'Evento")
    descrizione = models.TextField(verbose_name="Descrizione dettagliata")
    luogo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Luogo")

    class Meta:
        verbose_name_plural = "Biografie"

    def __construct__(self):
        return f"{self.data_evento} - {self.titolo_evento}"
    
class Partecipante(models.Model):
    # Collega il partecipante a uno specifico concerto
    concerto = models.ForeignKey(Concerto, on_delete=models.CASCADE, related_name='partecipanti')
    nome_completo = models.CharField(max_length=200)
    email = models.EmailField()
    codice_biglietto = models.CharField(max_length=100, unique=True)
    data_acquisto = models.DateTimeField(auto_now_add=True)
    # NUOVO CAMPO: Controlla se il biglietto è già passato ai tornelli
    utilizzato = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome_completo} - {self.concerto.luogo} (Usato: {self.utilizzato})"

# class VideoSpettacolo(models.Model):
#     titolo = models.CharField(max_length=200)
#     descrizione = models.TextField(blank=True, null=True)
#     # Aggiungiamo blank=True e null=True per gestire i vecchi dati senza blocchi
#     file_video = models.FileField(upload_to='video/', blank=True, null=True, help_text="Carica un file video (es. formato .mp4)")
#     data_aggiunta = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.titolo
    
#     class Meta:
#         verbose_name_plural = "Video Spettacoli"

class Video_Gallery(models.Model):
    """
    Relazione Uno-a-Molti: Una Biografia può avere PIÙ video locali caricati sul server.
    """
    biografia = models.ForeignKey(Biografia, on_delete=models.CASCADE, related_name='videos', verbose_name="Collegato all'evento")
    titolo_video = models.CharField(max_length=200, verbose_name="Titolo del Video")
    
    # MODIFICA QUI: Sostituito URLField con FileField per caricare i file .mp4
    file_video = models.FileField(
        max_length=255, 
        upload_to='videos/', 
        verbose_name="File Video (Formato MP4 consigliato)",
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name_plural = "Video Gallery"

    def __str__(self):
        return self.titolo_video


class Foto_Gallery(models.Model):
    """
    Relazione Uno-a-Molti: Una Biografia può avere PIÙ foto collegate.
    """
    biografia = models.ForeignKey(Biografia, on_delete=models.CASCADE, related_name='fotos', verbose_name="Collegato all'evento")
    titolo_foto = models.CharField(max_length=200, blank=True, verbose_name="Didascalia Foto")
    immagine = models.ImageField(max_length=255, upload_to='gallery/', verbose_name="File Immagine")

    class Meta:
        verbose_name_plural = "Foto Gallery"       
    
