from django.db import models

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
    titolo_sezione = models.CharField(max_length=200, default="La Storia")
    testo_completo = models.TextField()
    anno_inizio_carriera = models.IntegerField(default=1964)
    foto_artista = models.ImageField(upload_to='biografia/', blank=True, null=True)

    def __str__(self):
        return self.titolo_sezione
    
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

class VideoSpettacolo(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True, null=True)
    # Aggiungiamo blank=True e null=True per gestire i vecchi dati senza blocchi
    file_video = models.FileField(upload_to='video/', blank=True, null=True, help_text="Carica un file video (es. formato .mp4)")
    data_aggiunta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name_plural = "Video Spettacoli"

    
