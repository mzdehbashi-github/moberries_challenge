from django.contrib import admin

from pizza.models.pizza_flavour import PizzaFlavour


@admin.register(PizzaFlavour)
class PizzaFlavourAdmin(admin.ModelAdmin):
    pass
