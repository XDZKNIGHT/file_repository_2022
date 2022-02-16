# Generated by Django 3.2.5 on 2022-02-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_archivefile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='id',
        ),
        migrations.AddField(
            model_name='archivefile',
            name='file_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='file_id',
            field=models.BigAutoField(default='0', primary_key=True, serialize=False),
        ),
    ]