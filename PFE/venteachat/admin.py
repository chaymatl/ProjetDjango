from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Responsable_vente_et_achat)
admin.site.register(Fournisseur)
admin.site.register(Article)
admin.site.register(Client)
admin.site.register(Bon_de_commande)
admin.site.register(Bon_de_commande_vente)
admin.site.register(Bon_de_commande_achat)