from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Dish, DishType, Cook


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks']


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name']


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ['username', 'first_name', 'last_name', 'email', 'years_of_experience']


class RegisterForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ['username', 'first_name', 'last_name', 'email', 'years_of_experience']
