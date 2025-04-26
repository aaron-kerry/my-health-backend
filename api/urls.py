from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UtilisateurViewSet, RendezVousViewSet, DonDeSangViewSet,
                    TraitementMedicalViewSet, SpecialiteViewSet, VisiteViewSet)

router = DefaultRouter()
router.register(r'users', UtilisateurViewSet)
router.register(r'rendezvous', RendezVousViewSet)
router.register(r'donsang', DonDeSangViewSet)
router.register(r'medications', TraitementMedicalViewSet)
router.register(r'specialites', SpecialiteViewSet)
router.register(r'visites', VisiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
