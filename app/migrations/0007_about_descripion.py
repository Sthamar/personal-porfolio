# Generated by Django 5.1.2 on 2024-10-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profile_expertise_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='descripion',
            field=models.TextField(blank=True),
        ),
    ]
