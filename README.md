# Propiedades y Reservas - Backend API

Este proyecto es una API REST para gestionar propiedades, reservas y su disponibilidad. Está desarrollada en Flask y utiliza MongoDB como base de datos.

---

## **Requisitos**

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8+**
- **Pip** (gestor de paquetes de Python)
- **MongoDB** (puede ser local o en la nube)
- **Git** (para clonar el repositorio)

---

## **Configuración Inicial Backend**

1. **Clonar el repositorio**
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>

# Crear entorno Virtual
  python -m venv venv
  .\venv\Scripts\activate

# Instalar dependencias
  pip install -r requirements.txt

# Variables de entorno
  MONGO_URI=mongodb://localhost:27017
  DB_NAME=propiedades_db
  FLASK_ENV=development
  SECRET_KEY=your_secret_key
# ejecucion
  python main.py

## **Configuración Inicial Frontend**
    Npm install

# Variables de entorno en frontend
  VITE_API_URL = http://127.0.0.1:5000


