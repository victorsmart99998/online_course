# Generated by Django 5.0.1 on 2024-02-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0005_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]