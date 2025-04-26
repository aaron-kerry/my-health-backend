from rest_framework import serializers
from .models import Utilisateur, RendezVous, DonDeSang, TraitementMedical, Specialite, Visite

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'type', 'date_naissance', 'telephone']

class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'

class DonDeSangSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonDeSang
        fields = '__all__'

class TraitementMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraitementMedical
        fields = '__all__'

class SpecialiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = '__all__'

class VisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visite
        fields = '__all__'

