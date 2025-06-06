# Generated by Django 5.2 on 2025-05-08 15:05

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nom', models.CharField(db_column='nom', max_length=50)),
                ('prenom', models.CharField(db_column='prenom', max_length=50)),
                ('username', models.CharField(db_column='pseudo', max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('type', models.CharField(choices=[('Patient', 'Patient'), ('Professionnel', 'Professionnel'), ('Admin', 'Admin')], max_length=20)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'utilisateur',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DonDeSang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe_sanguin', models.CharField(max_length=3)),
                ('date_don', models.DateTimeField()),
                ('quantite', models.IntegerField()),
                ('lieu', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe_sanguin', models.CharField(max_length=3)),
                ('adresse', models.TextField(blank=True, null=True)),
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('Autre', 'Autre')], max_length=10, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('assurance_maladie', models.CharField(blank=True, max_length=50, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('antecedents', models.TextField(blank=True, null=True)),
                ('contact_urgence_nom', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_urgence_telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rdv', models.DateTimeField()),
                ('lieu', models.CharField(max_length=100)),
                ('duree', models.IntegerField(default=30)),
                ('statut', models.CharField(choices=[('Planifié', 'Planifié'), ('Confirmé', 'Confirmé'), ('Annulé', 'Annulé'), ('Terminé', 'Terminé')], default='Planifié', max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rdv_patient', to=settings.AUTH_USER_MODEL)),
                ('professionnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rdv_professionnel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='specialiste_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TraitementMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicament', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
                ('frequence', models.CharField(max_length=50)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visite', models.DateTimeField()),
                ('compte_rendu', models.TextField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professionnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visites_professionnel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
