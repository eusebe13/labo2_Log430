## Contexte
Nous avons besoin d’un ORM pour manipuler la base de données de manière déclarative, tout en gardant un contrôle SQL lorsque nécessaire.

## Décision
Nous avons choisi **SQLAlchemy**.

## Justification
- Intégration native avec FastAPI
- Large adoption dans l’écosystème Python
- Supporte à la fois ORM et requêtes SQL brutes
- Compatible avec plusieurs bases de données (SQLite, PostgreSQL, etc.)

## Conséquences
- Syntaxe plus complexe que d’autres ORM simples comme TortoiseORM
- Requiert une bonne organisation du modèle pour éviter la duplication