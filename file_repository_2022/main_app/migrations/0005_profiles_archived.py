# Generated by Django 3.2.5 on 2022-02-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]