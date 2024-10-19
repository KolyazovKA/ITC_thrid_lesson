from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.book.title}: {self.rating}"


class Storage(models.Model):
    amount = models.PositiveIntegerField('Количество')
    price = models.PositiveIntegerField('Стоимость')
    book = models.OneToOneField(Book, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Книга")

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Слады"

    def __str__(self):
        return f"{self.book.title} ({self.amount}): {self.price} руб."