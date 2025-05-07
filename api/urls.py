from .views import RegisterView, PatientViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, RendezVousViewSet, DonDeSangViewSet, TraitementMedicalViewSet, SpecialiteViewSet, VisiteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UtilisateurViewSet

router = DefaultRouter()
router.register(r'users', UtilisateurViewSet)
router.register(r'rendezvous', RendezVousViewSet)
router.register(r'donsang', DonDeSangViewSet)
router.register(r'medications', TraitementMedicalViewSet)
router.register(r'specialites', SpecialiteViewSet)
router.register(r'visites', VisiteViewSet)
router.register(r'patients', PatientViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
