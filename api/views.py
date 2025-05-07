from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Utilisateur,Patient
from .serializers import UtilisateurSerializer, RendezVousSerializer, DonDeSangSerializer,TraitementMedicalSerializer, SpecialiteSerializer, VisiteSerializer, PatientSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from .models import Utilisateur, RendezVous, DonDeSang, TraitementMedical, Specialite, Visite



# @method_decorator(csrf_exempt, name='dispatch')
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]  


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
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

class RegisterView(APIView):
    permission_classes = []  

    def post(self, request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)