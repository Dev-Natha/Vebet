# Generated by Django 5.0.1 on 2024-01-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0004_alter_profile_balance_alter_profile_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
