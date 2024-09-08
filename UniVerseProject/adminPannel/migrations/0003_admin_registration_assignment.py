# Generated by Django 5.0.6 on 2024-08-01 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0002_remove_admin_registration_email_and_more'),
        ('assignments_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_registration',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assignments_manager.assignmentdetails'),
        ),
    ]
