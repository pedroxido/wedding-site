# Generated by Django 2.0.10 on 2019-01-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorlax', '0003_auto_20190123_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
