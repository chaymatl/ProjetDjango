from django.db import models

# Create your models here.

class Administrateur(models.Model):
    nom = models.CharField(max_length=190, null=True)
    prénom = models.CharField(max_length=190, null=True)
    email = models.EmailField(max_length=20)
    mot_de_passe = models.CharField(max_length=190, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    CATEGORY = {
        ('Responsable_vente_et_achat','Responsable_vente_et_achat'),
        ('analyste_vente', 'analyste_vente'),
        ('analyste_achat', 'analyste_achat'),
    }
    nom = models.CharField(max_length=190, null=True)
    prénom = models.CharField(max_length=190, null=True)
    email = models.EmailField(max_length=20)
    mot_de_passe = models.CharField(max_length=190, null=True) 
    category = models.CharField(max_length=190, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Gère(models.Model):
    STATUS = { 
        ('created', 'created'),
        ('updated', 'updated'),
        ('delete', 'delete'),
        }
    administrateur = models.ForeignKey(Administrateur, null=True, on_delete=models.SET_NULL)
    utilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=190, null=True, choices=STATUS)
    
   

class kes(models.Model):

    nkes = models.AutoField(primary_key=True)
    nomkes=  models.CharField(max_length=20 , unique=True , null=False  ) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    

   

    


