# Configuración de Google Maps API

Para habilitar la funcionalidad de mapas en Pura Pata, necesitas una API key de Google Maps.

## Paso 1: Crear un proyecto en Google Cloud

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Nombre sugerido: "Pura Pata"

## Paso 2: Habilitar las APIs necesarias

1. Ve a "APIs & Services" > "Library"
2. Busca y habilita las siguientes APIs:
   - **Maps JavaScript API**
   - **Geocoding API** (opcional, para convertir direcciones a coordenadas)

## Paso 3: Crear credenciales

1. Ve a "APIs & Services" > "Credentials"
2. Clic en "Create Credentials" > "API key"
3. Copia la API key generada

## Paso 4: Configurar restricciones (Importante para seguridad)

1. En la lista de API keys, clic en tu nueva key
2. En "Application restrictions", selecciona "HTTP referrers (web sites)"
3. Agrega los siguientes referrers:
   ```
   https://pura-pata.fast-blocks.xyz/*
   https://pura-pata-51b0645355f2.herokuapp.com/*
   http://localhost:8000/*  (para desarrollo local)
   ```
4. En "API restrictions", selecciona "Restrict key"
5. Selecciona solo las APIs que habilitaste:
   - Maps JavaScript API
   - Geocoding API (si la habilitaste)

## Paso 5: Configurar en Heroku

```bash
heroku config:set GOOGLE_MAPS_API_KEY="TU_API_KEY_AQUI"
```

## Paso 6: Actualizar los templates

### Editar `templates/dogs/dog_form.html`

En la línea ~185, reemplaza:
```javascript
// NOTA: Necesitas una API key de Google Maps
// Descomenta la siguiente línea y agrega tu API key
// <script src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY&callback=initMap" async defer></script>
```

Por:
```javascript
<script src="https://maps.googleapis.com/maps/api/js?key={{ GOOGLE_MAPS_API_KEY }}&callback=initMap" async defer></script>
```

### Editar `templates/dogs/dog_detail.html`

En la línea ~130, reemplaza:
```javascript
// NOTA: Necesitas una API key de Google Maps
// Descomenta y agrega tu API key
// <script src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY&callback=initDogMap" async defer></script>
```

Por:
```javascript
<script src="https://maps.googleapis.com/maps/api/js?key={{ GOOGLE_MAPS_API_KEY }}&callback=initDogMap" async defer></script>
```

## Paso 7: Agregar la API key al contexto (Opcional)

### Editar `purapata/settings.py`

Agregar al final del archivo:
```python
# Google Maps
GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY', default='')
```

### Crear un context processor

Crear archivo `purapata/context_processors.py`:
```python
from django.conf import settings

def google_maps(request):
    return {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
```

### Actualizar TEMPLATES en settings.py

En la sección `TEMPLATES`, agregar el context processor:
```python
'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'purapata.context_processors.google_maps',  # <-- Agregar esta línea
],
```

## Costos

- Google Maps ofrece **$200 USD de crédito gratis** mensualmente
- Para un sitio pequeño/mediano, esto es más que suficiente
- No necesitas tarjeta de crédito para empezar (plan gratuito)

## Alternativa: Sin API Key

Si prefieres no usar Google Maps por ahora:
- Los formularios seguirán funcionando sin el mapa
- Los usuarios pueden dejar los campos de latitud/longitud vacíos
- La ubicación se mostrará solo con ciudad y estado

## Documentación oficial

- [Get Started with Google Maps Platform](https://developers.google.com/maps/get-started)
- [Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview)
