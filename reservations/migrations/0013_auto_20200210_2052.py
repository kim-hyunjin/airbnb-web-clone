# Generated by Django 2.2.9 on 2020-02-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_auto_20200203_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('confirmed', 'Comfirmed')], default='pending', max_length=12),
        ),
    ]
