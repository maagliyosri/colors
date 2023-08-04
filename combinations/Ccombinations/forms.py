from django import forms
from .models import Color,Voiture,FormulePeinture,Marque

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        color=forms.ModelChoiceField(queryset=Color.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        fields = ['name', 'hex_code']

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields=['nom','annee_fabrication','marque'] 

class FormulePeintureForm(forms.ModelForm):
    class Meta:
        model=FormulePeinture
        fields=['code_couleur','base_teint1','quantite_base_teint1','base_teint2','quantite_base_teint2',
         'base_teint3', 'quantite_base_teint3']        

class MarqueForm(forms.ModelForm):
    class Meta:
        model=Marque
        fields=['nom']