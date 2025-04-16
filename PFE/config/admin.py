from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Administrateur)
admin.site.register(Utilisateur)
admin.site.register(Gère)
admin.site.register(kes)


