from django.contrib import admin

from pizza.models.pizza_order_basket import PizzaOrderBasket


@admin.register(PizzaOrderBasket)
class PizzaOrderBasketAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at']
