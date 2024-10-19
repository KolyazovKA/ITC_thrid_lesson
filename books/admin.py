from django.contrib import admin
from books import models


# Register your models here.
@admin.register(models.Author)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "birthdate",
    )


@admin.register(models.Review)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "review_text",
        "rating",
    )


@admin.register(models.Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published_date",
    )


@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "price",
        "book"
    )