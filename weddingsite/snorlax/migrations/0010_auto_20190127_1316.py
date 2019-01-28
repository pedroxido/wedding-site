# Generated by Django 2.0.10 on 2019-01-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorlax', '0009_person_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='person',
        ),
        migrations.RemoveField(
            model_name='person',
            name='confirmation_status',
        ),
        migrations.AddField(
            model_name='person',
            name='meal',
            field=models.CharField(choices=[('MEAL_1', 'Meal Option 1'), ('MEAL_2', 'Meal Option 2'), ('MEAL_3', 'Meal Option 3')], default='MEAL_1', max_length=20, verbose_name='meal options'),
        ),
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, verbose_name='dietary restrictions'),
        ),
        migrations.AddField(
            model_name='person',
            name='rsvp_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='RSVP date'),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'Accept'), ('DECLINED', 'Decline')], default='DECLINED', max_length=9, verbose_name='status'),
        ),
        migrations.DeleteModel(
            name='RSVP',
        ),
    ]
