from django.db import models

NOM_CHOIX = [
        ('', 'Sélectionner une option'),
        ('mobile', 'Développement Mobile'),
        ('web', 'Développement Web'),
        ('logiciel', 'Logiciel'),
        ('Denade','Autre Demande')
]

# Create your models here.
class Blog(models.Model):
    Nom = models.CharField(max_length=255 , verbose_name="Nom")
    Email = models.EmailField(max_length=255)
    Entreprise = models.CharField(max_length=255,unique=True)
    Type_projet = models.Choices(choices=NOM_CHOIX,label="Type de développement")
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    lastcreated = models.DateTimeField(auto_now=True)