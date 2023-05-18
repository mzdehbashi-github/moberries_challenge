from django.contrib import admin

from pizza.models.pizza_size import PizzaSize


@admin.register(PizzaSize)
class PizzaSizeAdmin(admin.ModelAdmin):
    pass
