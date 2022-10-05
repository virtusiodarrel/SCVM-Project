# Generated by Django 4.1.1 on 2022-10-04 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QueryService', '0009_remove_bdsa_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdsa',
            name='added_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]