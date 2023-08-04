from django.urls import path
from .views import color_create, color_list,voiture_list,chercher_voiture,recherche_voiture

urlpatterns = [
    path('colors/create/', color_create, name='color_create'),
    path('colors/', color_list, name='color_list'),
    path('colors/a/', voiture_list, name='voiture_list'),
    path('colors/voiture/', chercher_voiture,name="chercher_voiture"),
    path('colors/recherche/', recherche_voiture,name="recherche_voiture"),



 
]