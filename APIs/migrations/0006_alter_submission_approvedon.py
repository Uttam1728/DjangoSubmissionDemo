# Generated by Django 3.2.11 on 2022-01-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0005_alter_submission_approvedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='ApprovedOn',
            field=models.DateField(blank=True, null=True),
        ),
    ]
