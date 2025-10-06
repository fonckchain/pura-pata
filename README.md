# Pura Pata 🐕

Plataforma web para la adopción de perros callejeros en México. Conecta refugios, rescatistas independientes y personas con perros disponibles para adopción.

## Características

- 🏠 Gestión de refugios y organizaciones de rescate
- 🐶 Publicación de perros disponibles para adopción
- 📸 Galería de fotos para cada perro
- 🔍 Búsqueda y filtrado de perros por características
- 👤 Sistema de usuarios para publicadores
- 📱 Diseño responsive con Bootstrap 5

## Tecnologías

- Python 3.12+
- Django 5.2
- PostgreSQL
- Bootstrap 5
- Crispy Forms

## Requisitos Previos

- Python 3.12 o superior
- PostgreSQL 12 o superior
- pip
- virtualenv

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/pura-pata.git
cd pura-pata
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

Crear la base de datos y usuario:

```sql
CREATE DATABASE purapata_db;
CREATE USER purapata_user WITH PASSWORD 'tu_contraseña';
ALTER ROLE purapata_user SET client_encoding TO 'utf8';
ALTER ROLE purapata_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE purapata_user SET timezone TO 'America/Mexico_City';
GRANT ALL PRIVILEGES ON DATABASE purapata_db TO purapata_user;
```

### 5. Configurar variables de entorno

Copiar el archivo de ejemplo y configurar:

```bash
cp .env.example .env
```

Editar `.env` con tus credenciales:

```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
DATABASE_NAME=purapata_db
DATABASE_USER=purapata_user
DATABASE_PASSWORD=tu_contraseña
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 6. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear superusuario

```bash
python manage.py createsuperuser
```

### 8. Crear directorios para archivos estáticos y media

```bash
mkdir -p static media
```

### 9. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El sitio estará disponible en: `http://localhost:8000`

El panel de administración en: `http://localhost:8000/admin`

## Estructura del Proyecto

```
pura-pata/
├── purapata/           # Configuración principal del proyecto
├── dogs/              # App para gestión de perros
├── shelters/          # App para gestión de refugios
├── static/            # Archivos estáticos (CSS, JS)
├── media/             # Archivos subidos por usuarios
├── templates/         # Templates HTML globales
├── requirements.txt   # Dependencias del proyecto
└── manage.py         # Script de gestión de Django
```

## Modelos Principales

### Dog (Perro)
- Información básica: nombre, raza, edad, tamaño, sexo, color
- Salud: vacunado, esterilizado, desparasitado
- Fotos: hasta 4 imágenes por perro
- Estado: disponible, adoptado, reservado

### Shelter (Refugio)
- Información de contacto y ubicación
- Usuario responsable
- Estado activo/inactivo

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.

## Contacto

Para preguntas o sugerencias, por favor abre un issue en GitHub.
