# Generated by Django 4.1.4 on 2022-12-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KIPY_ADMIN', '0005_remove_users_scores_alter_users_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('Только идея', 'Только идея'), ('В поиске команды', 'В поиске команды'), ('В работе', 'В работе'), ('Проект завершен', 'Проект завершен'), ('Проект заморожен', 'Проект заморожен')], default='Только идея', max_length=20, verbose_name='Статус проекта'),
        ),
    ]