from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, unique=True)


    def __str__(self):
        return self.name
class Marque(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
class Voiture(models.Model):
    nom = models.CharField(max_length=100)
    annee_fabrication = models.IntegerField()
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    code = models.ManyToManyField(Color, related_name='voitures')
    def __str__(self):
        return self.nom
class FormulePeinture(models.Model):
    code_couleur = models.ForeignKey(Color, on_delete=models.CASCADE)
    base_teint1 = models.CharField(max_length=50)
    quantite_base_teint1 = models.FloatField()
    base_teint2 = models.CharField(max_length=50, blank=True, null=True)
    quantite_base_teint2 = models.FloatField(blank=True, null=True)
    base_teint3 = models.CharField(max_length=50, blank=True, null=True)
    quantite_base_teint3 = models.FloatField(blank=True, null=True)