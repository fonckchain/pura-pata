# Pura Pata 🐕

Plataforma web para la adopción de perros callejeros en México. Conecta refugios, rescatistas independientes y personas con perros disponibles para adopción.

## 🌐 Sitio en Vivo

**URL:** [https://pura-pata.fast-blocks.xyz](https://pura-pata.fast-blocks.xyz)

## Características

- 🔐 **Sistema de autenticación**: Registro, login y gestión de usuarios
- 🏠 **Gestión de refugios**: Organizaciones de rescate y refugios pueden registrarse
- 🐶 **Publicación de perros**: Usuarios autenticados pueden publicar perros en adopción
- 📸 **Galería de fotos**: Hasta 4 imágenes por perro
- 🗺️ **Integración con Google Maps**: Ubicación geográfica de los perros
- 📍 **Geolocalización**: Coordenadas y dirección de cada perro
- 📞 **Información de contacto**: Teléfono y email para cada publicación
- 🔍 **Búsqueda y filtrado**: Por características, ubicación y estado
- 👤 **Panel de usuario**: Gestión de publicaciones propias
- 📱 **Diseño responsive**: Bootstrap 5 para todos los dispositivos
- 💬 **Sistema de mensajes**: Notificaciones flash para feedback al usuario

## Tecnologías

- Python 3.12+
- Django 5.2
- PostgreSQL
- Bootstrap 5
- Crispy Forms

### Dog (Perro)
- Información básica: nombre, raza, edad, tamaño, sexo, color
- Salud: vacunado, esterilizado, desparasitado
- Fotos: hasta 4 imágenes por perro
- Ubicación: dirección, ciudad, estado, coordenadas GPS
- Contacto: teléfono y email del publicador
- Estado: disponible, adoptado, reservado

### Shelter (Refugio)
- Información de contacto y ubicación
- Usuario responsable
- Estado activo/inactivo

## 🚀 Funcionalidades para Usuarios

### Visitantes (Sin autenticación)
- Ver listado de perros disponibles
- Ver detalles completos de cada perro
- Ver ubicación en mapa (Google Maps)
- Ver información de contacto

### Usuarios Registrados
- Todas las funcionalidades de visitantes
- Publicar perros en adopción
- Gestionar sus propias publicaciones
- Editar información de perros publicados
- Marcar ubicación en mapa interactivo

### Administradores
- Acceso completo al panel de Django Admin
- Gestión de todos los usuarios
- Gestión de todos los perros y refugios
- Moderación de contenido

## 🗺️ Configuración de Google Maps

El sitio está preparado para integración con Google Maps. Ver [GOOGLE_MAPS_SETUP.md](GOOGLE_MAPS_SETUP.md) para instrucciones detalladas.

## 📝 Uso del Sitio

1. **Registrarse**: Crea una cuenta desde "Registrarse"
2. **Iniciar Sesión**: Accede con tus credenciales
3. **Publicar Perro**: Click en "Publicar Perro" en el navbar
4. **Llenar Formulario**:
   - Información básica del perro
   - Estado de salud
   - Subir fotos (mínimo 1 foto principal)
   - Marcar ubicación en el mapa
   - Información de contacto
5. **Gestionar Publicaciones**: En "Mis Perros" puedes ver y editar tus publicaciones

## Licencia

Este proyecto está bajo la Licencia MIT.
