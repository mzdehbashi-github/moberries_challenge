from django.contrib import admin

from pizza.models.pizza_order_item import PizzaOrderItem


@admin.register(PizzaOrderItem)
class PizzaOrderItemAdmin(admin.ModelAdmin):
    pass
