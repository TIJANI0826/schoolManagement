# Generated by Django 2.2.5 on 2020-07-19 09:32

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=userprofile.models.user_directory_path),
        ),
    ]
