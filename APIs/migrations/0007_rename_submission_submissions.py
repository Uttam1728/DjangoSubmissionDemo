# Generated by Django 3.2.11 on 2022-01-09 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0006_alter_submission_approvedon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Submission',
            new_name='Submissions',
        ),
    ]
