# Generated by Django 5.0.1 on 2024-01-07 14:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0008_profile_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4),
        ),
    ]
