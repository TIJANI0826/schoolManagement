# Generated by Django 2.2.5 on 2020-07-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20200719_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.ManyToManyField(to='userprofile.Course'),
        ),
    ]
