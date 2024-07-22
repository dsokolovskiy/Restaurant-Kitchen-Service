from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Dish, DishType, Cook
from .forms import DishForm, DishTypeForm, CookForm


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dishes"


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(CreateView):
    model = Dish
    template_name = "kitchen/dish_form.html"
    fields = ["name", "description", "price", "dish_type", "cooks"]
    title = "Create Dish"


class DishUpdateView(UpdateView):
    model = Dish
    template_name = "kitchen/dish_form.html"
    fields = ["name", "description", "price", "dish_type", "cooks"]
    title = "Update Dish"


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = "/kitchen/dishes/"


class CookListView(ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cooks"


class CookDetailView(DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(CreateView):
    model = Cook
    template_name = "kitchen/cook_form.html"
    fields = ["username", "email", "password", "first_name", "last_name", "years_of_experience"]
    title = "Create Cook"


class CookUpdateView(UpdateView):
    model = Cook
    template_name = "kitchen/cook_form.html"
    fields = ["username", "email", "password", "first_name", "last_name", "years_of_experience"]
    title = "Update Cook"


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = "/kitchen/cooks/"
