# Generated by Django 4.2.1 on 2023-06-16 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_mahasiswa_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengcekan',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
