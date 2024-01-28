# Generated by Django 5.0 on 2024-01-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=10, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=10, max_digits=9),
            preserve_default=False,
        ),
    ]
