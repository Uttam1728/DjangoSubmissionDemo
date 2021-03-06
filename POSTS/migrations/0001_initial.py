# Generated by Django 3.2.11 on 2022-01-17 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('PostId', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Discription', models.JSONField()),
                ('Status', models.IntegerField(choices=[(0, 'Submited'), (1, 'Approved'), (2, 'Published')], default=0)),
                ('CreatedOn', models.DateField(auto_now_add=True)),
                ('LastUpdatedOn', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('AttachmentID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('URL', models.CharField(max_length=500)),
                ('AlterTitle', models.CharField(default='alter', max_length=500)),
                ('Post', models.ForeignKey(db_column='PostID', on_delete=django.db.models.deletion.CASCADE, to='POSTS.post')),
            ],
        ),
    ]
