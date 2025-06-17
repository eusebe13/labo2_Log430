## Contexte
Nous avons besoin d’une base de données légère, facile à configurer localement pour une application de point de vente (POS).

## Décision
Nous utilisons **SQLite** comme base de données.

## Justification
- Aucune configuration serveur requise
- Idéal pour une application monoposte ou petites instances POS locales
- Compatible avec SQLAlchemy
- Facile à tester, transférer ou sauvegarder

## Conséquences
- Ne convient pas pour la scalabilité horizontale ou la charge multi-utilisateurs
- Migration vers PostgreSQL envisageable si besoin