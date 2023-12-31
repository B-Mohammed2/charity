# Generated by Django 4.2.5 on 2023-09-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_hub', '0004_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='charity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='charity',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
