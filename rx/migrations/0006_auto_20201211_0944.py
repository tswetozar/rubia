# Generated by Django 3.1.3 on 2020-12-11 09:44

from django.db import migrations, models
import rx.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rx', '0005_auto_20201211_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rx',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, validators=[rx.validators.contains_only_letters, rx.validators.offensive_word]),
        ),
        migrations.AlterField(
            model_name='rx',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, validators=[rx.validators.contains_only_letters, rx.validators.offensive_word]),
        ),
    ]