from django.contrib import admin
from products import models
from users.models import User


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )


@admin.register(models.ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )


@admin.register(models.Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "comment",
    )


@admin.register(models.Basket)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
    )


@admin.register(models.User)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "fio",
        "email",
        "password",
    )
