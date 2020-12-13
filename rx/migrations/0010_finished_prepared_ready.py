# Generated by Django 3.1.3 on 2020-12-12 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rx', '0009_onhold_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ready',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=160)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rx.rx')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prepared',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=160)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rx.rx')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Finished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=160)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rx.rx')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]