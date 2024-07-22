from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    groups = models.ManyToManyField(
        Group,
        related_name="cooks",
        blank=True,
        help_text="The groups this cook belongs to.",
        related_query_name="cook",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="cooks",
        blank=True,
        help_text="Specific permissions for this cook.",
        related_query_name="cook",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.years_of_experience} years)"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return self.name
