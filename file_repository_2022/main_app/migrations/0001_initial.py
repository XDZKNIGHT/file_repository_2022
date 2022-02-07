# Generated by Django 4.0.1 on 2022-02-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('profile_picture', models.ImageField(blank=True, default='user_profile.png', upload_to='')),
                ('username', models.CharField(max_length=30)),
                ('eMail', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('security_question', models.CharField(max_length=100)),
                ('security_answer', models.CharField(max_length=100)),
                ('admin', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]