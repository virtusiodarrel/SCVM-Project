# Generated by Django 4.1.1 on 2022-10-04 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QueryService', '0008_rename_date_added_bdsa_added_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdsa',
            name='added_date',
        ),
    ]