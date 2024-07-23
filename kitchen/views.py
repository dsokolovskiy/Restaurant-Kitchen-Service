from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Dish, DishType, Cook
from .forms import DishForm, DishTypeForm, CookForm, CookCreationForm


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"


class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish_list")


class DishTypeListView(ListView):
    model = DishType
    template_name = "kitchen/dishtype_list.html"


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = "kitchen/dishtype_detail.html"


class DishTypeCreateView(CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dishtype_form.html"


class DishTypeUpdateView(UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dishtype_form.html"


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = "kitchen/dishtype_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dishtype_list")


class CookListView(ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"


class CookDetailView(DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"


class CookCreateView(CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook_list")


class CookUpdateView(UpdateView):
    model = Cook
    form_class = CookForm
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook_list")


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook_list")
