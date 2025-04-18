# Generated by Django 4.2.16 on 2025-03-31 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_completed',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/background_images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_images/'),
        ),
    ]
