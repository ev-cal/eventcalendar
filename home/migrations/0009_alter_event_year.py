# Generated by Django 4.0.2 on 2022-03-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_event_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='year',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]
