# Generated by Django 3.1.5 on 2021-01-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
