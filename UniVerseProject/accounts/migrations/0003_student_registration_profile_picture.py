# Generated by Django 5.0.6 on 2024-07-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student_registration_admission_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_registration',
            name='profile_picture',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
