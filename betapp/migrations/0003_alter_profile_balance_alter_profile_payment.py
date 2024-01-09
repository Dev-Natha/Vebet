# Generated by Django 5.0.1 on 2024-01-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='payment',
            field=models.ImageField(null=True, upload_to='paymentpic'),
        ),
    ]
