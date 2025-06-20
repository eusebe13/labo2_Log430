# Utilise une image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . .

# Exposer un port si ton app a une API FastAPI par exemple
EXPOSE 8000

# Commande à exécuter au lancement du conteneur
CMD ["python", "app/init_db.py"]
