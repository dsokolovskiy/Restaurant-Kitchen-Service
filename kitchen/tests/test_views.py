from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.models import Dish, DishType, Cook
from kitchen.forms import DishForm, DishTypeForm, CookForm


User = get_user_model()


class DishViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.dish_type = DishType.objects.create(name='Starter')
        self.dish = Dish.objects.create(
            name='Salad',
            description='Fresh vegetable salad',
            price=9.99,
            dish_type=self.dish_type,
        )
        self.client.login(username='testuser', password='12345')

    def test_dish_list_view(self):
        response = self.client.get(reverse('kitchen:dish_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_list.html')
        self.assertContains(response, 'Salad')

    def test_dish_detail_view(self):
        response = self.client.get(reverse('kitchen:dish_detail', args=[self.dish.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_detail.html')
        self.assertContains(response, 'Salad')

    def test_dish_create_view(self):
        response = self.client.get(reverse('kitchen:dish_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_create.html')

        response = self.client.post(reverse('kitchen:dish_create'), {
            'name': 'Pasta',
            'description': 'Delicious pasta',
            'price': 12.99,
            'dish_type': self.dish_type.pk,
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного створення
        self.assertEqual(Dish.objects.count(), 2)

    def test_dish_update_view(self):
        response = self.client.get(reverse('kitchen:dish_update', args=[self.dish.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_update.html')

        response = self.client.post(reverse('kitchen:dish_update', args=[self.dish.pk]), {
            'name': 'Updated Salad',
            'description': 'Updated description',
            'price': 10.99,
            'dish_type': self.dish_type.pk,
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного оновлення
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, 'Updated Salad')

    def test_dish_delete_view(self):
        response = self.client.get(reverse('kitchen:dish_delete', args=[self.dish.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_delete.html')

        response = self.client.post(reverse('kitchen:dish_delete', args=[self.dish.pk]))
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного видалення
        self.assertEqual(Dish.objects.count(), 0)


class DishTypeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.dish_type = DishType.objects.create(name='Starter')
        self.client.login(username='testuser', password='12345')

    def test_dishtype_list_view(self):
        response = self.client.get(reverse('kitchen:dishtype_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_list.html')
        self.assertContains(response, 'Starter')

    def test_dishtype_detail_view(self):
        response = self.client.get(reverse('kitchen:dishtype_detail', args=[self.dish_type.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_detail.html')
        self.assertContains(response, 'Starter')

    def test_dishtype_create_view(self):
        response = self.client.get(reverse('kitchen:dishtype_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_create.html')

        response = self.client.post(reverse('kitchen:dishtype_create'), {
            'name': 'Dessert',
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного створення
        self.assertEqual(DishType.objects.count(), 2)

    def test_dishtype_update_view(self):
        response = self.client.get(reverse('kitchen:dishtype_update', args=[self.dish_type.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_update.html')

        response = self.client.post(reverse('kitchen:dishtype_update', args=[self.dish_type.pk]), {
            'name': 'Updated Starter',
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного оновлення
        self.dish_type.refresh_from_db()
        self.assertEqual(self.dish_type.name, 'Updated Starter')

    def test_dishtype_delete_view(self):
        response = self.client.get(reverse('kitchen:dishtype_delete', args=[self.dish_type.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_delete.html')

        response = self.client.post(reverse('kitchen:dishtype_delete', args=[self.dish_type.pk]))
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного видалення
        self.assertEqual(DishType.objects.count(), 0)


class CookViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cook = Cook.objects.create_user(username='cookuser', password='12345', years_of_experience=5)
        self.client.login(username='testuser', password='12345')

    def test_cook_list_view(self):
        response = self.client.get(reverse('kitchen:cook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_list.html')
        self.assertContains(response, 'cookuser')

    def test_cook_detail_view(self):
        response = self.client.get(reverse('kitchen:cook_detail', args=[self.cook.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_detail.html')
        self.assertContains(response, 'cookuser')

    def test_cook_create_view(self):
        response = self.client.get(reverse('kitchen:cook_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_create.html')

        response = self.client.post(reverse('kitchen:cook_create'), {
            'username': 'newcook',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'years_of_experience': 3,  # Включаємо years_of_experience
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного створення
        self.assertEqual(Cook.objects.count(), 2)

    def test_cook_update_view(self):
        response = self.client.get(reverse('kitchen:cook_update', args=[self.cook.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_update.html')

        response = self.client.post(reverse('kitchen:cook_update', args=[self.cook.pk]), {
            'username': 'updatedcook',
            'years_of_experience': 6,  # Включаємо years_of_experience
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного оновлення
        self.cook.refresh_from_db()
        self.assertEqual(self.cook.username, 'updatedcook')

    def test_cook_delete_view(self):
        response = self.client.get(reverse('kitchen:cook_delete', args=[self.cook.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/cook_delete.html')

        response = self.client.post(reverse('kitchen:cook_delete', args=[self.cook.pk]))
        self.assertEqual(response.status_code, 302)  # Перенаправлення після успішного видалення
        self.assertEqual(Cook.objects.count(), 0)
