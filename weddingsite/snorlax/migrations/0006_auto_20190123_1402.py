# Generated by Django 2.0.10 on 2019-01-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorlax', '0005_auto_20190123_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='meal',
            field=models.CharField(choices=[('MEAL_1', 'Meal Option 1'), ('MEAL_2', 'Meal Option 2'), ('MEAL_3', 'Meal Option 3')], max_length=20),
        ),
    ]