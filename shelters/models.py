from django.db import models
from django.contrib.auth.models import User


class Shelter(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    address = models.CharField(max_length=300, verbose_name="Dirección")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    state = models.CharField(max_length=100, verbose_name="Estado")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    website = models.URLField(blank=True, null=True, verbose_name="Sitio web")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Refugio"
        verbose_name_plural = "Refugios"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
