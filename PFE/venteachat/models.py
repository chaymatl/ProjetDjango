from django.db import models

# Create your models here.

class Responsable_vente_et_achat(models.Model):
    nom = models.CharField(max_length=190, null=True)
    prénom = models.CharField(max_length=190, null=True)
    email = models.CharField(max_length=190, null=True)
    mot_de_passe = models.CharField(max_length=190, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.nom


class Fournisseur(models.Model):
    nom = models.CharField(max_length=190, null=True)
    prénom = models.CharField(max_length=190, null=True)
    cin = models.CharField(max_length=190, null=True)
    num_tel = models.CharField(max_length=190, null=True)
    adresse = models.CharField(max_length=190, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom = models.CharField(max_length=190, null=True)
    prix_article = models.PositiveIntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=190, null=True)
    prénom = models.CharField(max_length=190, null=True)
    cin =  models.CharField(max_length=190, null=True)
    num_tel = models.CharField(max_length=190, null=True)
    adresse = models.CharField(max_length=190, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom 

class Bon_de_commande(models.Model):
    
    nom = models.CharField(max_length=190, null=True)
    date = models.CharField(max_length=190, null=True)
    prix = models.IntegerField(blank=True , null=True )
    quantité = models.IntegerField(blank=True , null=True )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

class Bon_de_commande_vente(models.Model):
    montant_de_vente= models.IntegerField(blank=True , null=True )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Bon_de_commande_achat(models.Model):
    montant_achat=models.IntegerField(blank=True , null=True )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Gère(models.Model):
    STATUS = { 
        ('created', 'created'),
        ('updated', 'updated'),
        ('delete', 'delete'),
        }
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=190, null=True, choices=STATUS)
    responsable_vente_et_achat = models.ForeignKey(Responsable_vente_et_achat, null=True, on_delete=models.SET_NULL)
    fournisseur = models.ForeignKey(Fournisseur, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    bon_de_commande = models.ForeignKey(Bon_de_commande, null=True, on_delete=models.SET_NULL)
    bon_de_commande_vente = models.ForeignKey(Bon_de_commande_vente, null=True, on_delete=models.SET_NULL)
    bon_de_commande_achat= models.ForeignKey(Bon_de_commande_achat, null=True, on_delete=models.SET_NULL)
    


    
    