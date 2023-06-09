# Generated by Django 4.1.7 on 2023-04-01 07:46

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170410_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdb',
            name='resume',
            field=models.FileField(blank=True, upload_to=student.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='appliedjob',
            name='got_offer',
            field=models.CharField(default='No', max_length=250),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='s_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
