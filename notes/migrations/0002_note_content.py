# Generated by Django 3.1.7 on 2021-03-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
