# Generated by Django 3.2.11 on 2022-01-09 08:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtable',
            name='TestjsonFeild',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
    ]
