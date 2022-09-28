# Generated by Django 4.1.1 on 2022-09-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryService', '0005_remove_bdsa_id_alter_bdsa_cve_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdsa',
            name='content',
        ),
        migrations.RemoveField(
            model_name='bdsa',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bdsa',
            name='mitigation',
        ),
        migrations.RemoveField(
            model_name='bdsa',
            name='patch_links',
        ),
        migrations.RemoveField(
            model_name='bdsa',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='bdsa',
            name='technical_description',
        ),
        migrations.RemoveField(
            model_name='bdsa',
            name='vul_function',
        ),
        migrations.AddField(
            model_name='bdsa',
            name='json_raw',
            field=models.TextField(default='', verbose_name='json_raw'),
            preserve_default=False,
        ),
    ]
