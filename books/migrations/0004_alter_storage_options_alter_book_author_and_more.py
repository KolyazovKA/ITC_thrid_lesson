# Generated by Django 5.1.2 on 2024-10-23 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_published_date_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storage',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Слады'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]