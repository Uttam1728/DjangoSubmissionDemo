# Generated by Django 3.2.11 on 2022-01-09 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0009_auto_20220109_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='SubmissionID',
        ),
        migrations.AddField(
            model_name='attachment',
            name='Submission',
            field=models.ForeignKey(db_column='SubmissionID', default=None, on_delete=django.db.models.deletion.CASCADE, to='APIs.submission'),
            preserve_default=False,
        ),
    ]
