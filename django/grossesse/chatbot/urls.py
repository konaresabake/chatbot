from django.urls import path
from .views import*

app_name = 'chatbot'  # Namespace pour vos URLs

urlpatterns = [
    # Page d'accueil du chatbot
    path('', chatbot_view, name='chatbot_view'),
    
]