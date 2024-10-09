from django.db import models


class User(models.Model):
    # Модель для примера. Вообще лучше через AbstractUser наследоваться
    fio = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to="users_images", null=True, blank=True)

    def __str__(self) -> str:
        return self.fio
