from django.db import models
from django.contrib.auth.models import User
from shelters.models import Shelter


class Dog(models.Model):
    SIZE_CHOICES = [
        ('pequeño', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]

    GENDER_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]

    STATUS_CHOICES = [
        ('disponible', 'Disponible'),
        ('adoptado', 'Adoptado'),
        ('reservado', 'Reservado'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    age_years = models.IntegerField(verbose_name="Edad (años)", help_text="Edad aproximada en años")
    age_months = models.IntegerField(default=0, verbose_name="Edad (meses)", help_text="Meses adicionales")
    breed = models.CharField(max_length=100, verbose_name="Raza", help_text="Raza o mezcla")
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, verbose_name="Tamaño")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Sexo")
    color = models.CharField(max_length=100, verbose_name="Color")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponible', verbose_name="Estado")

    # Características de salud
    vaccinated = models.BooleanField(default=False, verbose_name="Vacunado")
    sterilized = models.BooleanField(default=False, verbose_name="Esterilizado")
    dewormed = models.BooleanField(default=False, verbose_name="Desparasitado")
    special_needs = models.TextField(blank=True, null=True, verbose_name="Necesidades especiales")

    # Imágenes
    photo_main = models.ImageField(upload_to='dogs/', verbose_name="Foto principal")
    photo_1 = models.ImageField(upload_to='dogs/', blank=True, null=True, verbose_name="Foto 1")
    photo_2 = models.ImageField(upload_to='dogs/', blank=True, null=True, verbose_name="Foto 2")
    photo_3 = models.ImageField(upload_to='dogs/', blank=True, null=True, verbose_name="Foto 3")

    # Relaciones
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, null=True, blank=True,
                               related_name='dogs', verbose_name="Refugio")
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Publicado por")

    # Ubicación
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="Dirección")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ciudad")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Latitud")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Longitud")

    # Contacto
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono de contacto")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="Email de contacto")

    # Metadatos
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Perro"
        verbose_name_plural = "Perros"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_age_display(self):
        """Retorna la edad en formato legible"""
        if self.age_months > 0:
            return f"{self.age_years} años, {self.age_months} meses"
        return f"{self.age_years} años"

    def get_location(self):
        """Retorna la ubicación completa"""
        parts = []
        if self.city:
            parts.append(self.city)
        if self.state:
            parts.append(self.state)
        return ", ".join(parts) if parts else "Sin ubicación"

    def has_coordinates(self):
        """Verifica si tiene coordenadas para mostrar en mapa"""
        return self.latitude is not None and self.longitude is not None
