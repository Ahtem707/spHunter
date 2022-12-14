# Generated by Django 4.0.7 on 2022-10-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KIPY_ADMIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(verbose_name='Чат ID')),
                ('message_id', models.CharField(max_length=200, verbose_name='ID Сообщений')),
            ],
            options={
                'verbose_name': 'Удаление сообщений',
                'verbose_name_plural': 'Удаление сообщений',
                'db_table': 'delete_message',
            },
        ),
    ]
