from django.contrib import admin

from pizza.models.customer import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
