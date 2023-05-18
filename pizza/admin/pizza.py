from django.contrib import admin

from pizza.models.pizza import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_select_related = ['flavour', 'size']
