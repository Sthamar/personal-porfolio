# Generated by Django 5.1.2 on 2024-10-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_descripion_about_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_summary',
            field=models.TextField(blank=True),
        ),
    ]
