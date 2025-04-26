from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import Utilisateur, RendezVous, DonDeSang, TraitementMedical, Specialite, Visite
from .serializers import (UtilisateurSerializer, RendezVousSerializer, DonDeSangSerializer,
                           TraitementMedicalSerializer, SpecialiteSerializer, VisiteSerializer)

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]

class RendezVousViewSet(viewsets.ModelViewSet):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer
    permission_classes = [permissions.IsAuthenticated]

class DonDeSangViewSet(viewsets.ModelViewSet):
    queryset = DonDeSang.objects.all()
    serializer_class = DonDeSangSerializer
    permission_classes = [permissions.IsAuthenticated]

class TraitementMedicalViewSet(viewsets.ModelViewSet):
    queryset = TraitementMedical.objects.all()
    serializer_class = TraitementMedicalSerializer
    permission_classes = [permissions.IsAuthenticated]

class SpecialiteViewSet(viewsets.ModelViewSet):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    permission_classes = [permissions.IsAuthenticated]

class VisiteViewSet(viewsets.ModelViewSet):
    queryset = Visite.objects.all()
    serializer_class = VisiteSerializer
    permission_classes = [permissions.IsAuthenticated]