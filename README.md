# My Health Backend

Application backend pour la gestion de services de santé développée avec Django et Django REST Framework.

## Table des matières

- [Description](#description)
- [Architecture du projet](#architecture-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [API Documentation](#api-documentation)
- [Développement](#développement)
- [Licence](#licence)

## Description

My Health Backend est une API RESTful développée pour gérer des services de santé, permettant aux utilisateurs de consulter et gérer des informations médicales de manière sécurisée.

## Architecture du projet

```
my-health-backend/
├── api/                      # Application Django pour les endpoints API
├── backend_project/          # Projet Django principal (settings, urls, etc.)
│   ├── __init__.py
│   ├── settings.py           # Configuration du projet
│   ├── urls.py               # Configuration des URLs du projet
│   ├── asgi.py
│   └── wsgi.py
├── manage.py                 # Script de gestion Django
├── myhealth/                 # Environnement virtuel (ne pas inclure dans Git)
└── requirements.txt          # Dépendances du projet
```

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Virtualenv (recommandé)

## Installation

1. Clonez le dépôt:

```bash
git clone https://github.com/aaron-kerry/my-health-backend.git
cd my-health-backend
```

2. Créez un environnement virtuel:

```bash
python -m venv myhealth
```

3. Activez l'environnement virtuel:

**Sous Linux/macOS:**
```bash
source myhealth/bin/activate
```

**Sous Windows:**
```bash
myhealth\Scripts\activate
```

4. Installez les dépendances:

```bash
pip install -r requirements.txt
```

## Configuration

1. Effectuez les migrations de la base de données:

```bash
python manage.py migrate
```

2. Créez un super utilisateur pour accéder à l'interface d'administration:

```bash
python manage.py createsuperuser
```

## Utilisation

1. Lancez le serveur de développement:

```bash
python manage.py runserver
```

2. Accédez à l'application:
   - API: http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/
   - Page d'accueil: http://localhost:8000/

## API Documentation

La documentation de l'API est disponible via Swagger UI et ReDoc:

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/
- Documentation JSON: http://localhost:8000/swagger.json

### Points d'accès principaux

- `/api/` - Point d'entrée principal de l'API
- `/admin/` - Interface d'administration Django
- `/swagger/` - Documentation interactive de l'API (Swagger UI)
- `/redoc/` - Documentation alternative de l'API (ReDoc)

## Développement

### Commandes utiles

- Lister les commandes disponibles:
```bash
python manage.py help
```

- Créer une nouvelle application:
```bash
python manage.py startapp nom_app
```

- Effectuer des migrations après modification de modèles:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Lancer les tests:
```bash
python manage.py test
```

### Structure des applications

Chaque application Django devrait suivre une structure similaire:

```
api/
├── __init__.py
├── admin.py          # Configuration de l'admin Django
├── apps.py           # Configuration de l'application
├── migrations/       # Migrations de base de données
├── models.py         # Modèles de données
├── serializers.py    # Sérialiseurs REST Framework
├── tests.py          # Tests unitaires
└── views.py          # Vues et ViewSets
```

## Licence

Ce projet est sous licence [Insérer votre licence ici] - voir le fichier LICENSE pour plus de détails.