# Generated by Django 4.0.2 on 2022-02-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_name', models.CharField(max_length=30)),
                ('uploader', models.CharField(max_length=30)),
            ],
        ),
    ]