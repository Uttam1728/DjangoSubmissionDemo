# Generated by Django 3.2.11 on 2022-01-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('TestId', models.AutoField(primary_key=True, serialize=False)),
                ('TestCharFeild', models.CharField(max_length=50)),
            ],
        ),
    ]
