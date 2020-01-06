# Generated by Django 2.2.8 on 2020-01-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20200106_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Comfirmed'), ('canceled', 'Canceled')], default='pending', max_length=12),
        ),
    ]
