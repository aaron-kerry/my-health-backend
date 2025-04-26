from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    TYPES = (
        ('Patient', 'Patient'),
        ('Professionnel', 'Professionnel'),
        ('Admin', 'Admin')
    )
    type = models.CharField(max_length=20, choices=TYPES)
    date_naissance = models.DateField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)

class RendezVous(models.Model):
    STATUTS = (
        ('Planifié', 'Planifié'),
        ('Confirmé', 'Confirmé'),
        ('Annulé', 'Annulé'),
        ('Terminé', 'Terminé')
    )
    patient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='rdv_patient')
    professionnel = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='rdv_professionnel')
    date_rdv = models.DateTimeField()
    lieu = models.CharField(max_length=100)
    duree = models.IntegerField(default=30)
    statut = models.CharField(max_length=20, choices=STATUTS, default='Planifié')

class DonDeSang(models.Model):
    patient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    groupe_sanguin = models.CharField(max_length=3)
    date_don = models.DateTimeField()
    quantite = models.IntegerField()
    lieu = models.CharField(max_length=100)

class TraitementMedical(models.Model):
    patient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    medicament = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequence = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

class Specialite(models.Model):
    nom = models.CharField(max_length=100)

class Visite(models.Model):
    patient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    professionnel = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='visites_professionnel')
    date_visite = models.DateTimeField()
    compte_rendu = models.TextField(blank=True, null=True)






