## Contexte
Le backend de notre application doit fournir une API REST rapide, lisible, et facile à maintenir. Il doit s'intégrer avec une base de données locale SQLite via ORM.

## Décision
Nous avons choisi **FastAPI** pour développer le backend Python.

## Justification
- Excellente performance (asynchrone, basé sur Starlette)
- Documentation automatique avec Swagger (OpenAPI)
- Typage clair grâce à Pydantic
- Intégration simple avec SQLAlchemy
- Démarrage rapide et courbe d’apprentissage douce

## Conséquences
- Les développeurs doivent être familiers avec les concepts asynchrones (async/await)
- Déploiement via Uvicorn ou Gunicorn conseillé en production