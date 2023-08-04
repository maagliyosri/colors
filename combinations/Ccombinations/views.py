from django.shortcuts import render, redirect
from .models import Color,Voiture,FormulePeinture,Marque
from .forms import ColorForm,VoitureForm,FormulePeintureForm,MarqueForm

def color_create(request):

    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('color_list')
    else:
        form = ColorForm()
    return render(request, 'color_create.php', {'form': form})



def color_list(request):
    colors = Color.objects.all()
    return render(request, 'color_list.php', {'colors': colors})

def voiture_create(request):
    if request.method == 'POST':
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voiture_list')
    else:
        form = ColorForm()
    return render(request, 'color_create.php', {'form': form})
def voiture_list(request):
    voitures = Voiture.objects.all()
    return render(request, 'color_list.php', {'voitures': voitures})


def chercher_voiture(request):
    if request.method == 'POST':
        hex_code = request.POST.get('hex_code', '')
        nom = request.POST.get('nom', '')
        voiture = Voiture.objects.filter(nom__iexact=nom).first()
        couleur = Color.objects.filter(hex_code__iexact=hex_code).first()
        formule_peinture= None
        formule_peinture1=None
        if voiture is not None and couleur is not None:
            formule_peinture = FormulePeinture.objects.get(code_couleur=voiture.code)
        elif voiture:
            formule_peinture = FormulePeinture.objects.get(code_couleur=voiture.code)
        elif couleur:
            formule_peinture1=FormulePeinture.objects.filter(code_couleur=couleur.id)






        return render(request, 'chercher_voiture.html',{'couleur':couleur,'voiture':voiture,'formule_peinture1': formule_peinture1,'formule_peinture': formule_peinture})
    else:
        return render(request, 'chercher_voiture.html')    




def recherche_voiture(request):
    if request.method == 'POST':
        nom_voiture = request.POST.get('nom')
        code_couleur = request.POST.get('hex_code')
        marque_voiture = request.POST.get('nom')
        if nom_voiture and code_couleur:
            voitures = Voiture.objects.filter(nom__icontains=nom_voiture, code__hex_code__icontains=code_couleur)
            couleur_cherchee = Color.objects.filter(hex_code=code_couleur).first()
            marques = Marque.objects.filter(nom=marque_voiture).first()
        elif nom_voiture:
            voitures = Voiture.objects.filter(nom__icontains=nom_voiture)
            couleur_cherchee = Color.objects.filter(hex_code=code_couleur).first()

        elif code_couleur:
            voitures = Voiture.objects.filter(code__hex_code__icontains=code_couleur)
            couleur_cherchee = Color.objects.filter(hex_code=code_couleur).first()

        else:
            voitures = []
            couleur_cherchee = None

        context = {'voitures': voitures, 'nom_voiture': nom_voiture,'couleur_cherchee': couleur_cherchee}
        return render(request, 'recherche_voiture.html', context)

    return render(request, 'recherche_voiture.html')





def get_formule_peinture(self):
        formule = FormulePeinture.objects.get( code=self.code)
        return formule        