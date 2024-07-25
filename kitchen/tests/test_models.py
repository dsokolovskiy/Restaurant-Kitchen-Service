from django.test import TestCase
from kitchen.models import DishType, Dish, Cook


from django.contrib.auth import get_user_model


class DishTypeModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Appetizer")

    def test_dish_type(self):
        self.assertEqual(str(self.dish_type), "Appetizer")


class CookModelTest(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.cook = self.user_model.objects.create_user(
            username="chef",
            first_name="John",
            last_name="Doe",
            years_of_experience=5,
            password="testpassword"
        )

    def test_cook_str(self):
        self.assertEqual(
            str(self.cook),
            f"John Doe (5 years)"
        )


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = get_user_model().objects.create_user(
            username="chef",
            first_name="John",
            last_name="Doe",
            years_of_experience=5,
            password="testpassword"
        )
        self.dish = Dish.objects.create(
            name="Spaghetti",
            description="Delicious spaghetti with tomato sauce.",
            price=12.99,
            dish_type=self.dish_type,
            image=None
        )
        self.dish.cooks.add(self.cook)

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Spaghetti")

    def test_dish_type_relationship(self):
        self.assertEqual(self.dish.dish_type.name, "Main Course")

    def test_dish_cooks_relationship(self):
        self.assertIn(self.cook, self.dish.cooks.all())
