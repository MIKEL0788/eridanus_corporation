from django.db import models

NOM_CHOIX = [
        ('', 'Sélectionner une option'),
        ('mobile', 'Développement Mobile'),
        ('web', 'Développement Web'),
        ('logiciel', 'Logiciel'),
        ('Denade','Autre Demande')
]

# Create your models here.
class Formulaire(models.Model):
    Nom = models.CharField(max_length=255 , verbose_name="Nom")
    Email = models.EmailField(max_length=255)
    Entreprise = models.CharField(max_length=255,unique=True)
    
    type_demande = models.CharField(
        max_length=50,
        choices=NOM_CHOIX,
        default=''    
    )
    
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    lse3astcreated = models.DateTimeField(auto_now=True)