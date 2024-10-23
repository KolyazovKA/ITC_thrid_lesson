import factory

from books import models

class AuthorFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    birthdate = factory.Faker('date_of_birth', minimum_age=18, maximum_age=120)
    class Meta:
        model = models.Author

class BookFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    published_date = factory.Faker('date')
    author = factory.SubFactory(AuthorFactory)
    class Meta:
        model = models.Book
