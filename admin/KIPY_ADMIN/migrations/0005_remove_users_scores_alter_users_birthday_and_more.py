# Generated by Django 4.0.7 on 2022-12-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KIPY_ADMIN', '0004_practice_users_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='scores',
        ),
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения пользователя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mail',
            field=models.EmailField(max_length=100, null=True, verbose_name='Почта'),
        ),
    ]