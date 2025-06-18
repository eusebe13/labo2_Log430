# ADR-005 : Choix du linter pour le projet

## Contexte

Pour maintenir une bonne qualité de code et appliquer des règles de style cohérentes dans notre projet Python, il est indispensable d'utiliser un outil de linting efficace. Plusieurs options sont disponibles dans l'écosystème Python.

## Décision

Nous choisissons **Ruff** comme outil principal de linting pour ce projet.

## Justification

- **Performance exceptionnelle** : Ruff est écrit en Rust et est extrêmement rapide, permettant un linting instantané même sur de gros projets.
- **Polyvalence** : Ruff intègre les fonctionnalités de nombreux autres linters (comme Flake8, Pyflakes, pycodestyle, Mypy pour certains contrôles, etc.) en un seul outil.
- **Configuration simple** : Ruff utilise un fichier de configuration simple (`pyproject.toml` ou `.ruff.toml`).
- **Support actif** : Ruff bénéficie d'une communauté croissante et d'un développement actif.
- **Facilité d'intégration** : S'intègre facilement dans les pipelines CI/CD et les éditeurs de code.

## Conséquences

- Tous les développeurs devront installer Ruff et s'assurer que le code passe le linting avant de pousser.
- Le pipeline CI/CD inclura une étape de linting avec Ruff qui devra passer pour autoriser les merges.
- Certaines règles peuvent être activées ou désactivées via la configuration, offrant flexibilité et contrôle.
- L’utilisation de Ruff permettra de réduire le temps passé au linting, accélérant les boucles de développement.

## Alternatives considérées

| Alternative | Avantages                      | Inconvénients                        |
|-------------|-------------------------------|------------------------------------|
| Flake8      | Large écosystème, extensible  | Plus lent, configuration parfois lourde |
| Pylint      | Très complet et rigoureux     | Plus lent, verbose                  |
| Black       | Formatage automatique         | Ne fait pas de linting classique   |

## Références

- [Ruff Documentation](https://beta.ruff.rs/)
- [Comparaison Ruff vs Flake8](https://beta.ruff.rs/docs/comparison/)
