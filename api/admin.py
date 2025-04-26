# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    model = Utilisateur
    list_display = ['username', 'email', 'type', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('type', 'date_naissance', 'telephone')}),
    )
