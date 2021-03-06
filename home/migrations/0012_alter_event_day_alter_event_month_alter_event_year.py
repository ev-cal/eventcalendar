# Generated by Django 4.0.2 on 2022-03-06 07:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_event_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2)]),
        ),
    ]
