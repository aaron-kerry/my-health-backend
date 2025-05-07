from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Utilisateur(AbstractUser):
    TYPES = (
        ('Patient', 'Patient'),
        ('Professionnel', 'Professionnel'),
        ('Admin', 'Admin')
    )
    type = models.CharField(max_length=20, choices=TYPES)
    date_naissance = models.DateField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)

class Patient(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_profile')
    
    groupe_sanguin = models.CharField(max_length=3)
    adresse = models.TextField(blank=True, null=True)
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')], blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    assurance_maladie = models.CharField(max_length=50, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    antecedents = models.TextField(blank=True, null=True)
    contact_urgence_nom = models.CharField(max_length=100, blank=True, null=True)
    contact_urgence_telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Profil Patient: {self.utilisateur.get_full_name()}"


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






