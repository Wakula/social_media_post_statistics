# Generated by Django 3.2.6 on 2021-08-07 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('post_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('likes_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('acquired_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
