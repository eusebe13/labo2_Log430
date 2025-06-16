#!/bin/bash

# Lancer l'initialisation de la base de données
echo "Initialisation de la base de données..."
cd backend || exit 1
python app/init_db.py
if [ $? -ne 0 ]; then
    echo "Échec de l'initialisation de la base de données."
    exit 1
fi

# Lancer le backend avec uvicorn
echo "Démarrage du backend avec Uvicorn..."
uvicorn app.main:app --reload &
BACKEND_PID=$!
cd ..

# Lancer le frontend
echo "Démarrage du frontend..."
cd frontend || exit 1
npm run dev &
FRONTEND_PID=$!
cd ..

# Gérer l'arrêt propre (Ctrl+C)
trap "echo 'Arrêt en cours...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
