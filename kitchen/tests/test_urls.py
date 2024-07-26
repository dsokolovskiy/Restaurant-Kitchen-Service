from django.test import SimpleTestCase
from django.urls import reverse, resolve

from kitchen.views import (
    HomePageView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeListView,
)


class UrlsTest(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_dish_list_url_is_resolved(self):
        url = reverse('kitchen:dish_list')
        self.assertEqual(resolve(url).func.view_class, DishListView)

    def test_dish_detail_url_is_resolved(self):
        url = reverse('kitchen:dish_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, DishDetailView)

    def test_cook_list_url_is_resolved(self):
        url = reverse('kitchen:cook_list')
        self.assertEqual(resolve(url).func.view_class, CookListView)

    def test_cook_detail_url_is_resolved(self):
        url = reverse('kitchen:cook_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, CookDetailView)

    def test_dish_type_list_url_is_resolved(self):
        url = reverse('kitchen:dishtype_list')
        self.assertEqual(resolve(url).func.view_class, DishTypeListView)
