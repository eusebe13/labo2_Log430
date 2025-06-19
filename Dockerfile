# Utilise une image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement les fichiers nécessaires au départ
COPY backend/requirements.txt ./backend/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copier tout le contenu du projet
COPY backend/ ./backend/

# Exposer le port pour FastAPI
EXPOSE 8000

# Commande à exécuter au lancement du conteneur
CMD ["python", "backend/app/main.py"]
