from rest_framework import serializers
from .models import Utilisateur, RendezVous, DonDeSang, TraitementMedical, Specialite, Visite, Patient 

class UtilisateurSerializer(serializers.ModelSerializer):
    prenom = serializers.CharField(source='first_name')
    nom = serializers.CharField(source='last_name')
    mot_de_passe = serializers.CharField(write_only=True, source='password')

    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'email', 'prenom', 'nom',
            'mot_de_passe', 'type', 'date_naissance', 'telephone'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')

        user = Utilisateur.objects.create_user(
            password=password,
            first_name=first_name,
            last_name=last_name,
            **validated_data
        )
        return user


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



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

