
1. L’utilisation avec Docker.
2. L’utilisation via un **environnement virtuel Python** (venv).
3. Un lien avec `app/main.py` comme point d’entrée de l’application.
4. Des instructions pratiques pour l'utilisateur.

---

# labo1_Log430  
**Gestionnaire de ventes – Application distribuée en console**

---

## Modes d'exécution
```bash
# S'asssurer d'etre dans le bon dossier
~/labo1_Log430$
```
### 1. Exécution avec Docker

```bash
docker-compose build
docker-compose up
````

---

### 2. Exécution en local avec Python et un environnement virtuel (venv)

#### Prérequis :

* Python 3.12
* `pip`

#### Étapes :

```bash
# Créer et activer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# Lancer l'application
python app/main.py
```

---

## Lancer les tests

```bash
# Une fois dans le venv
pytest
```

---

## Linting (Analyse statique)


Ce projet utilise [Ruff](https://docs.astral.sh/ruff/) pour l’analyse statique du code :

```bash
# Vérifier le code
ruff check .

# Corriger automatiquement les erreurs détectées
ruff check . --fix
```

---

## Structure des dossiers

| Dossier  | Contenu                  |
| -------- | ------------------------ |
| `app/`   | Code source principal    |
| `tests/` | Tests unitaires          |
| `ADR/`   | Décisions d'architecture |
| `UML/`   | Diagrammes de conception |
| `docs/`  | Documentation technique  |

---

## Choix technologiques


| Outil      | Rôle / Justification                          |
| ---------- | --------------------------------------------- |
| Python     | Langage principal                             |
| SQLAlchemy | ORM robuste et flexible                       |
| PostgreSQL | Base de données fiable                        |
| Docker     | Exécution isolée, environnement reproductible |
| Ruff       | Lint rapide et moderne pour Python            |

---

## Makefile

Pour automatiser certaines tâches :

```makefile
lint:
	ruff check .

lint-fix:
	ruff check . --fix

test:
	pytest
```

connexion:
	Nom d'utilisateur: employe1
	Mot de passe: 1234
	
	Nom d'utilisateur: gestionnaire1
	Mot de passe: admin
	
	Nom d'utilisateur: responsable1
	Mot de passe: root

	Swagger UI est disponible ici :
	http://127.0.0.1:8000/docs

	Et ReDoc ici :
	http://127.0.0.1:8000/redoc
