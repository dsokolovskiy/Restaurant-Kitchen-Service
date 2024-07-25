from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import Dish, DishType, Cook
from kitchen.forms import DishForm, DishTypeForm, CookForm


User = get_user_model()


class DishViewTest(TestCase):

    def setUp(self):
        self.dish_type = DishType.objects.create(name='Appetizer')
        self.cook = Cook.objects.create_user(
            username='cookuser',
            password='password123',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            years_of_experience=5
        )
        self.dish = Dish.objects.create(
            name='Salad',
            description='A fresh salad.',
            price=5.99,
            dish_type=self.dish_type
        )
        self.client.login(username='cookuser', password='password123')

    def test_dish_list_view(self):
        response = self.client.get(reverse('kitchen:dish_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_list.html')
        self.assertContains(response, self.dish.name)
        self.assertContains(response, self.dish.description)

    def test_dish_detail_view(self):
        response = self.client.get(reverse('kitchen:dish_detail', args=[self.dish.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_detail.html')
        self.assertContains(response, self.dish.name)
        self.assertContains(response, self.dish.description)

    def test_dish_create_view(self):
        response = self.client.post(reverse('kitchen:dish_create'), {
            'name': 'Pasta',
            'description': 'A tasty pasta dish.',
            'price': 8.99,
            'dish_type': self.dish_type.pk,
            'cooks': [self.cook.pk]
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:dish_list'))
        self.assertTrue(Dish.objects.filter(name='Pasta').exists())

    def test_dish_update_view(self):
        response = self.client.post(reverse('kitchen:dish_update', args=[self.dish.pk]), {
            'name': 'Updated Salad',
            'description': 'An updated description.',
            'price': 6.99,
            'dish_type': self.dish_type.pk,
            'cooks': [self.cook.pk]
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:dish_list'))
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, 'Updated Salad')

    def test_dish_delete_view(self):
        response = self.client.post(reverse('kitchen:dish_delete', args=[self.dish.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:dish_list'))
        self.assertFalse(Dish.objects.filter(pk=self.dish.pk).exists())


class DishTypeViewTest(TestCase):

    def setUp(self):
        self.dish_type = DishType.objects.create(name='Appetizer')
        self.client.login(username='cookuser', password='password123')

    def test_dishtype_list_view(self):
        response = self.client.get(reverse('kitchen:dishtype_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_list.html')
        self.assertContains(response, self.dish_type.name)

    def test_dishtype_detail_view(self):
        response = self.client.get(reverse('kitchen:dishtype_detail', args=[self.dish_type.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_detail.html')
        self.assertContains(response, self.dish_type.name)

    def test_dishtype_create_view(self):
        response = self.client.post(reverse('kitchen:dishtype_create'), {
            'name': 'Dessert'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:dishtype_list'))
        self.assertTrue(DishType.objects.filter(name='Dessert').exists())

    def test_dishtype_update_view(self):
        response = self.client.post(reverse('kitchen:dishtype_update', args=[self.dish_type.pk]), {
            'name': 'Updated Appetizer'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:dishtype_list'))
        self.dish_type.refresh_from_db()
        self.assertEqual(self.dish_type.name, 'Updated Appetizer')

    def test_dishtype_delete_view(self):
        response = self.client.post(reverse('kitchen:dishtype_delete', args=[self.dish_type.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:dishtype_list'))
        self.assertFalse(DishType.objects.filter(pk=self.dish_type.pk).exists())


class CookViewTest(TestCase):

    def setUp(self):
        self.cook = Cook.objects.create_user(
            username='cookuser',
            password='password123',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            years_of_experience=5
        )
        self.client.login(username='cookuser', password='password123')

    def test_cook_list_view(self):
        response = self.client.get(reverse('kitchen:cook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_list.html')
        self.assertContains(response, self.cook.username)

    def test_cook_detail_view(self):
        response = self.client.get(reverse('kitchen:cook_detail', args=[self.cook.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_detail.html')
        self.assertContains(response, self.cook.username)

    def test_cook_create_view(self):
        response = self.client.post(reverse('kitchen:cook_create'), {
            'username': 'newcook',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'years_of_experience': 3
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:cook_list'))
        self.assertTrue(Cook.objects.filter(username='newcook').exists())

    def test_cook_update_view(self):
        response = self.client.post(reverse('kitchen:cook_update', args=[self.cook.pk]), {
            'username': 'updatedcook',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'years_of_experience': 10
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:cook_list'))
        self.cook.refresh_from_db()
        self.assertEqual(self.cook.years_of_experience, 10)

    def test_cook_delete_view(self):
        response = self.client.post(reverse('kitchen:cook_delete', args=[self.cook.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('kitchen:cook_list'))
        self.assertFalse(Cook.objects.filter(pk=self.cook.pk).exists())
