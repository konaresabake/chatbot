from django.db import models

class Interaction(models.Model):
    RISQUE_CHOICES = [
        ('normal', 'Normal'),
        ('modéré', 'Modéré'),
        ('élevé', 'Élevé'),
    ]
    
    date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    mois_grossesse = models.IntegerField()
    poids_kg = models.FloatField()
    taille_cm = models.FloatField()
    activite = models.CharField(max_length=20)
    regime = models.CharField(max_length=20)
    antecedents = models.CharField(max_length=20)
    symptome = models.CharField(max_length=20)
    profil_risque = models.CharField(max_length=10, choices=RISQUE_CHOICES)
    conseil = models.TextField()

    def __str__(self):
        return f"Interaction du {self.date.strftime('%Y-%m-%d')}"