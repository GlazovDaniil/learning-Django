# Generated by Django 5.0 on 2023-12-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='autor',
        ),
        migrations.AddField(
            model_name='books',
            name='autor',
            field=models.ManyToManyField(help_text='Выберете автора книги', to='catalog.autor', verbose_name='Автор книги'),
        ),
    ]
