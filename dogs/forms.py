from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = [
            'name', 'description', 'age_years', 'age_months', 'breed', 'size', 'gender', 'color',
            'vaccinated', 'sterilized', 'dewormed', 'special_needs',
            'photo_main', 'photo_1', 'photo_2', 'photo_3',
            'address', 'city', 'state', 'latitude', 'longitude',
            'contact_phone', 'contact_email', 'shelter'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del perro'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Cuéntanos sobre este perro...'}),
            'age_years': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'age_months': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 11}),
            'breed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza o mezcla'}),
            'size': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color del pelaje'}),
            'special_needs': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Opcional: necesidades especiales'}),
            'photo_main': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.FileInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección (opcional)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email de contacto'}),
            'shelter': forms.Select(attrs={'class': 'form-select'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
