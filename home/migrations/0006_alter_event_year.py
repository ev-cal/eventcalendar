# Generated by Django 4.0.2 on 2022-03-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_event_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
