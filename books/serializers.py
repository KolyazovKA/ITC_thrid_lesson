from rest_framework import serializers
from books import models


class Author(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class Book(serializers.ModelSerializer):
    author = Author(read_only=True)
    author_id = serializers.IntegerField(required=False, allow_null=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = models.Book
        fields = "__all__"

    def get_price(self, obj):
        if models.Storage.objects.filter(book=obj).exists():
            return obj.storage.price
        return None


class Review(serializers.ModelSerializer):
    book = Book(read_only=True)
    class Meta:
        model = models.Review
        fields = "__all__"


class Storage(serializers.ModelSerializer):
    book = Book(read_only=True)
    class Meta:
        model = models.Storage
        fields = "__all__"
