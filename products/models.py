from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.comment}"


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products_images", null=True, blank=True)
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        to=Comment, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product}: {self.quantity}"
