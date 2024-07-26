from django.contrib import admin
from .models import Dish, DishType, Cook

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'dish_type', 'get_cooks')
    search_fields = ('name',)
    list_filter = ('dish_type',)

    def get_cooks(self, obj):
        return ", ".join([cook.username for cook in obj.cooks.all()])
    get_cooks.short_description = 'Cooks'

class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CookAdmin(admin.ModelAdmin):
    list_display = ('username', 'years_of_experience')
    search_fields = ('username',)

admin.site.register(Dish, DishAdmin)
admin.site.register(DishType, DishTypeAdmin)
admin.site.register(Cook, CookAdmin)