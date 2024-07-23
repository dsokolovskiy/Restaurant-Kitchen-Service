from django.urls import path
from .views import (
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    HomePageView,
)

app_name = 'kitchen'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dishes/create/', DishCreateView.as_view(), name='dish_create'),
    path('dishes/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),

    path('dishtypes/', DishTypeListView.as_view(), name='dishtype_list'),
    path('dishtypes/<int:pk>/', DishTypeDetailView.as_view(), name='dishtype_detail'),
    path('dishtypes/create/', DishTypeCreateView.as_view(), name='dishtype_create'),
    path('dishtypes/<int:pk>/update/', DishTypeUpdateView.as_view(), name='dishtype_update'),
    path('dishtypes/<int:pk>/delete/', DishTypeDeleteView.as_view(), name='dishtype_delete'),

    path('cooks/', CookListView.as_view(), name='cook_list'),
    path('cooks/<int:pk>/', CookDetailView.as_view(), name='cook_detail'),
    path('cooks/create/', CookCreateView.as_view(), name='cook_create'),
    path('cooks/<int:pk>/update/', CookUpdateView.as_view(), name='cook_update'),
    path('cooks/<int:pk>/delete/', CookDeleteView.as_view(), name='cook_delete'),
]
