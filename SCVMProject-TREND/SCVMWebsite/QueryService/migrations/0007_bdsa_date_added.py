# Generated by Django 4.1.1 on 2022-10-04 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QueryService', '0006_remove_bdsa_content_remove_bdsa_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdsa',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]