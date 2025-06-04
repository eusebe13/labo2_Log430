# ADR 0001 - Architecture initiale

## Contexte

Nous devons développer une application distribuée en console qui permet d’interagir avec une base de données contenant des produits et des ventes.

## Décision

Utiliser une architecture modulaire Python avec une base de données sqlite conteneurisée.

## Conséquences

- Facilite les tests et déploiements.
- Simplifie l’évolution future vers une interface web si souhaité.
