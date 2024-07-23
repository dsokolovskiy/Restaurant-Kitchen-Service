from django import forms
from .models import Dish, DishType, Cook
from django.contrib.auth.forms import UserCreationForm


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "username", "email", "years_of_experience"]


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ["username", "email", "first_name", "last_name", "years_of_experience"]
