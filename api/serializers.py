from rest_framework import serializers
from .models import Utilisateur, RendezVous, DonDeSang, TraitementMedical, Specialite, Visite, Patient 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur  # Vous devez spécifier le modèle
        fields = ['id', 'username', 'nom', 'prenom', 'email', 'type', 'date_naissance', 'telephone', 'password']  # Ou listez les champs explicitement


    def create(self, validated_data):
        password = validated_data.pop('password')
        prenom = validated_data.pop('prenom')
        nom = validated_data.pop('nom')
        
        user = Utilisateur.objects.create_user(
            password=password,
            prenom=prenom,
            nom=nom,
            **validated_data
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Ajoutez des claims personnalisés
        token['type'] = user.type
        token['email'] = user.username
        token['mot_de_passe'] = user.email
        return token

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

