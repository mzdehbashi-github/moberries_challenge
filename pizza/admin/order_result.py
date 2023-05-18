from django.contrib import admin

from pizza.models.order_result import OrderResult


@admin.register(OrderResult)
class OrderResultAdmin(admin.ModelAdmin):
    list_display = ['basket_id', 'date', 'status']
