# Generated by Django 5.0.1 on 2024-05-24 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0012_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user_course',
        ),
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.course'),
        ),
    ]
