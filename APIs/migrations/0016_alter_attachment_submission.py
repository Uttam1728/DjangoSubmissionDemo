# Generated by Django 3.2.11 on 2022-01-17 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0015_alter_attachment_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='Submission',
            field=models.ForeignKey(db_column='SubmissionID', on_delete=django.db.models.deletion.CASCADE, to='APIs.submission'),
        ),
    ]
