from django import forms

class GrossesseForm(forms.Form):
    age = forms.IntegerField(label="Âge")
    mois_grossesse = forms.IntegerField(label="Mois de grossesse")
    poids_kg = forms.FloatField(label="Poids (kg)")
    taille_cm = forms.FloatField(label="Taille (cm)")
    ACTIVITE_CHOICES = [
        ('faible', 'Faible'),
        ('modérée', 'Modérée'),
        ('élevée', 'Élevée')
    ]
    activité = forms.ChoiceField(choices=ACTIVITE_CHOICES, label="Niveau d'activité physique")
    REGIME_CHOICES = [
        ('omnivore', 'Omnivore'),
        ('végétarien', 'Végétarien'),
        ('végétalien', 'Végétalien')
    ]
    régime = forms.ChoiceField(choices=REGIME_CHOICES, label="Régime alimentaire")
    ANTECEDENTS_CHOICES = [
        ('aucun', 'Aucun'),
        ('diabète', 'Diabète'),
        ('asthme', 'Asthme'),
        ('autre', 'Autre')
    ]
    antécédents = forms.ChoiceField(choices=ANTECEDENTS_CHOICES, label="Antécédents médicaux")
    SYMPTOME_CHOICES = [
        ('aucun', 'Aucun'),
        ('nausée', 'Nausée'),
        ('fatigue', 'Fatigue'),
        ('douleur', 'Douleur')
    ]
    symptôme = forms.ChoiceField(choices=SYMPTOME_CHOICES, label="Symptômes actuels")