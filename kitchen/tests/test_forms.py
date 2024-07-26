from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.forms import CookForm, RegisterForm, DishForm, DishTypeForm


from kitchen.models import Dish, DishType, Cook

User = get_user_model()


class FormTestCase(TestCase):
    def assert_form_invalid(self, form, expected_errors):
        self.assertFalse(form.is_valid())
        print(form.errors)
        for field in expected_errors:
            self.assertIn(field, form.errors)
        self.assertEqual(len(form.errors), len(expected_errors))


class CookFormTest(FormTestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'chef2',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'chef2@example.com',
            'years_of_experience': 3,
        }
        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'years_of_experience': '',
        }
        form = CookForm(data=form_data)
        self.assert_form_invalid(form, ['username', 'years_of_experience'])


class RegisterFormTest(FormTestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'new_chef',
            'first_name': 'Emma',
            'last_name': 'Johnson',
            'email': 'new_chef@example.com',
            'years_of_experience': 4,
            'password1': 'strongpassword',
            'password2': 'strongpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'years_of_experience': '',
            'password1': '',
            'password2': '',
        }
        form = RegisterForm(data=form_data)
        self.assert_form_invalid(form, ['username', 'years_of_experience', 'password1', 'password2'])

    def test_password_mismatch(self):
        form_data = {
            'username': 'new_chef2',
            'first_name': 'Noah',
            'last_name': 'Williams',
            'email': 'new_chef2@example.com',
            'years_of_experience': 1,
            'password1': 'password123',
            'password2': 'differentpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertIn('password2', form.errors)


class DishFormTest(FormTestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name='Appetizer')
        self.cook = Cook.objects.create(username='chef3', email='chef3@example.com', years_of_experience=5)

    def test_valid_form(self):
        form_data = {
            'name': 'Salad',
            'description': 'Fresh and healthy',
            'price': 10.00,
            'dish_type': self.dish_type.id,
            'cooks': [self.cook.id],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'name': '',
            'description': '',
            'price': '',
            'dish_type': '',
            'cooks': '',
        }
        form = DishForm(data=form_data)
        self.assert_form_invalid(form, ['name', 'description', 'price', 'dish_type', 'cooks'])


class DishTypeFormTest(FormTestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Main Course',
        }
        form = DishTypeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'name': '',
        }
        form = DishTypeForm(data=form_data)
        self.assert_form_invalid(form, ['name'])
