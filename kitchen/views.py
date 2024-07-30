from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Dish, DishType, Cook
from .forms import DishForm, DishTypeForm, CookForm, RegisterForm


class HomePageView(ListView):
    model = Dish
    template_name = 'kitchen/home.html'
    context_object_name = 'dishes'


class DishListView(ListView):
    model = Dish
    template_name = 'kitchen/dish_list.html'
    context_object_name = 'dish_list'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'kitchen/dish_detail.html'
    context_object_name = 'dish'


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'kitchen/dish_create.html'
    success_url = reverse_lazy('kitchen:dish_list')


class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'kitchen/dish_update.html'
    success_url = reverse_lazy('kitchen:dish_list')


class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'kitchen/dish_delete.html'
    success_url = reverse_lazy('kitchen:dish_list')


class DishTypeListView(ListView):
    model = DishType
    template_name = 'kitchen/dishtype_list.html'
    context_object_name = 'dishtype_list'


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = 'kitchen/dishtype_detail.html'
    context_object_name = 'dishtype'


class DishTypeCreateView(CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = 'kitchen/dishtype_create.html'
    success_url = reverse_lazy('kitchen:dishtype_list')


class DishTypeUpdateView(UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = 'kitchen/dishtype_update.html'
    success_url = reverse_lazy('kitchen:dishtype_list')


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = 'kitchen/dishtype_delete.html'
    success_url = reverse_lazy('kitchen:dishtype_list')


class CookListView(ListView):
    model = Cook
    template_name = 'kitchen/cook_list.html'
    context_object_name = 'cook_list'


class CookDetailView(DetailView):
    model = Cook
    template_name = 'kitchen/cook_detail.html'
    context_object_name = 'cook'


class CookCreateView(CreateView):
    model = Cook
    form_class = CookForm
    template_name = 'kitchen/cook_create.html'
    success_url = reverse_lazy('kitchen:cook_list')


class CookUpdateView(UpdateView):
    model = Cook
    form_class = CookForm
    template_name = 'kitchen/cook_update.html'
    success_url = reverse_lazy('kitchen:cook_list')


class CookDeleteView(DeleteView):
    model = Cook
    template_name = 'kitchen/cook_delete.html'
    success_url = reverse_lazy('kitchen:cook_list')


class RegisterView(CreateView):
    model = Cook
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
