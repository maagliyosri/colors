from django.contrib import admin

from .models import Color,Marque,Voiture,FormulePeinture
admin.site.register(Color)
admin.site.register(Marque)
admin.site.register(Voiture)
admin.site.register(FormulePeinture)