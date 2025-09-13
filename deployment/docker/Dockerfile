# Étape 1: Utiliser une image Python officielle
FROM python:3.10-slim

# Étape 2: Définir le répertoire de travail
WORKDIR /app

# Étape 3: Installer Poetry
RUN pip install poetry

# Étape 4: Copier les fichiers de dépendances
COPY pyproject.toml poetry.lock* ./

# Étape 5: Configurer le timeout ET LES TENTATIVES de pip, PUIS installer les dépendances
# C'est la ligne finale qui résout les problèmes de réseau instable
RUN pip config set global.timeout 900 && \
    pip config set global.retries 10 && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --without dev

# Étape 6: Copier le reste du code de l'application
COPY . .

# Étape 7: Exposer le port
EXPOSE 8000

# Étape 8: Commande pour lancer l'application
CMD ["poetry", "run", "uvicorn", "super_expert_comptable_v04.main:app", "--host", "0.0.0.0", "--port", "8000"]
