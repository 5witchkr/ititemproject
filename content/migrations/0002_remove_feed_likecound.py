# Generated by Django 3.2 on 2022-02-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='likeCound',
        ),
    ]
