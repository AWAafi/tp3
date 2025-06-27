FROM python:3.10-slim

# Installation des dépendances système nécessaires (par exemple pour Selenium, si utilisé avec Firefox)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Installer geckodriver (nécessaire pour Selenium + Firefox)
RUN wget -q https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.34.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.34.0-linux64.tar.gz

WORKDIR /app

# Copier les dépendances et installer les libs Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port Flask (optionnel mais recommandé)
EXPOSE 5000

CMD ["python", "app.py"]
