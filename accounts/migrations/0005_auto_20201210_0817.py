# Generated by Django 3.1.3 on 2020-12-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201210_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='card_number',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]
