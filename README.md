# Backend Technical Test - Task Manager API

API RESTful desarrollada con **Python (FastAPI)** y **PostgreSQL**, diseñada para gestionar tareas de forma eficiente, segura y escalable.

## Descripción del Proyecto

El sistema implementa un **CRUD completo** de tareas pendientes con autenticación basada en JWT.

El objetivo principal es construir una arquitectura modular que permita fácil mantenimiento y escalabilidad, separando responsabilidades entre rutas, lógica de negocio y acceso a datos.

## Stack Tecnológico

- **Python 3.11.8**
- **FastAPI**: Framework moderno de alto rendimiento.
- **PostgreSQL**: Persistencia de datos (ejecutado en Docker).
- **SQLAlchemy (ORM)**: Para la abstracción de base de datos.
- **Alembic**: Gestión de migraciones de base de datos.
- **Docker & Docker Compose**: Contenerización del entorno.

## Decisiones Técnicas y Arquitectura

### 1. Arquitectura Modular
Se evitó una estructura monolítica en favor de una organización por capas (`api`, `core`, `models`, `schemas`, `db`). Esto facilita la lectura del código, el testing y permite que el proyecto crezca sin volverse inmanejable.

### 2. FastAPI y Pydantic
La elección de FastAPI se debe a su manejo nativo de asincronía y la integración con Pydantic para la validación de datos. Esto reduce drásticamente el código repetitivo y garantiza que los datos de entrada y salida cumplan estrictamente con los contratos definidos.

### 3. Optimización de Base de Datos
Se definieron índices explícitos en la tabla `tasks` para los campos:
- `status`: Optimiza el filtrado frecuente por estado de la tarea.
- `created_at`: Mejora el rendimiento del ordenamiento en listas paginadas grandes.

### 4. Seguridad
- **Autenticación**: Implementación de OAuth2 con Password Flow y JWT.
- **Almacenamiento**: Las contraseñas se almacenan hasheadas utilizando el algoritmo **Bcrypt**, siguiendo estándares de seguridad actuales.
- **Autorización**: Los endpoints están protegidos para asegurar que un usuario solo pueda leer y modificar sus propias tareas.

## Instalación y Ejecución

### Prerrequisitos
- Tener **Docker** y **Docker Compose** instalados y el servicio corriendo.
- Python 3.10 o superior.

### Pasos para levantar el entorno de desarrollo local

```bash
# Clonar el repositorio
git clone https://github.com/JulianSanti28/backend-technical-test
cd backend-technical-test

# Crear y activar entorno virtual
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Levantar la base de datos con Docker
docker-compose up -d

# Aplicar migraciones de base de datos
alembic upgrade head

# Cargar usuario inicial
python -m app.initial_data

# Iniciar el servidor con reload para desarrollo ágil
uvicorn app.main:app --reload
```

Una vez iniciado el servidor, consulte la documentación interactiva de los endpoints en:

**http://127.0.0.1:8000/docs**