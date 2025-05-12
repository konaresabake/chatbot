from django.shortcuts import render
from .form import GrossesseForm
import joblib
from sklearn.preprocessing import LabelEncoder


def chatbot_view(request):
    if request.method == 'POST':
        form = GrossesseForm(request.POST)
        if form.is_valid():
            # Charger le modèle et les encodeurs
            model = joblib.load('C:\\Users\\HP\\Downloads\\chatbot\\django\\grossesse\\models_ml\\modele_grossesse.joblib')
            le_activite = joblib.load('C:\\Users\\HP\\Downloads\\chatbot\\django\\grossesse\\models_ml\\encodeur_activite.joblib')
            le_regime = joblib.load('C:\\Users\\HP\\Downloads\\chatbot\\django\\grossesse\\models_ml\\encodeur_regime.joblib')
            le_antecedents = joblib.load('C:\\Users\\HP\\Downloads\\chatbot\\django\\grossesse\\models_ml\\encodeur_antecedents.joblib')
            le_symptome = joblib.load('C:\\Users\\HP\\Downloads\\chatbot\\django\\grossesse\\models_ml\\encodeur_symptome.joblib')
            
            # Préparer les données pour la prédiction
            data = {
                'age': form.cleaned_data['age'],
                'mois_grossesse': form.cleaned_data['mois_grossesse'],
                'poids_kg': form.cleaned_data['poids_kg'],
                'taille_cm': form.cleaned_data['taille_cm'],
                'activité': le_activite.transform([form.cleaned_data['activité']])[0],
                'régime': le_regime.transform([form.cleaned_data['régime']])[0],
                'antécédents': le_antecedents.transform([form.cleaned_data['antécédents']])[0],
                'symptôme': le_symptome.transform([form.cleaned_data['symptôme']])[0]
            }
            
            # Faire la prédiction
            prediction = model.predict([list(data.values())])[0]
            
            # Générer le conseil en fonction du risque
            if prediction == 'normal':
                conseil = "Votre grossesse présente un risque normal. Continuez à avoir une alimentation équilibrée et à bien vous hydrater."
            elif prediction == 'modéré':
                conseil = "Votre grossesse présente un risque modéré. Nous vous conseillons de consulter votre médecin deux fois par mois et d'éviter les situations stressantes."
            else:  # élevé
                conseil = "Votre grossesse présente un risque élevé. Un suivi médical renforcé est nécessaire. Consultez immédiatement votre médecin pour un bilan complet."
            
            return render(request, 'chatbot/resultat.html', {'prediction': prediction, 'conseil': conseil})
    else:
        form = GrossesseForm()
    
    return render(request, 'chatbot/formulaire.html', {'form': form})