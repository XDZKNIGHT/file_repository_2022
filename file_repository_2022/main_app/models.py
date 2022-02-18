from email.policy import default
from django.db import models

class Profiles(models.Model):
    profile_picture = models.ImageField(null=False, blank=True, default='user_profile.png')
    username = models.CharField(max_length=30, null=False, blank=False)
    eMail = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    security_question = models.CharField(max_length=100, null=False, blank=False)
    security_answer = models.CharField(max_length=100, null=False, blank=False)
    admin = models.BooleanField(default=False, null=False)
    archived = models.BooleanField(default=False,null=False)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.username

class UploadedFile(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=30, null=False, blank=False)
    file_type = models.CharField(max_length=30, null=False, blank=False , default = 'file')
    uploader = models.CharField(max_length=30, null=False, blank=False)
    archived = models.BooleanField(default=False,null=False)
    uploaded_date = models.CharField(max_length=30, null=False, blank=False , default = 'date')
    file_id = models.BigAutoField(primary_key=True)

class Archive(models.Model):
    profile_picture = models.ImageField(null=False, blank=True, default='user_profile.png')
    username = models.CharField(max_length=30, null=False, blank=False)
    eMail = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    security_question = models.CharField(max_length=100, null=False, blank=False)
    security_answer = models.CharField(max_length=100, null=False, blank=False)
    admin = models.BooleanField(default=False, null=False)
    user_id = models.IntegerField(default='0')

    def __str__(self):
        return self.username

class ArchiveFile(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=30, null=False, blank=False)
    file_type = models.CharField(max_length=30, null=False, blank=False , default = 'file')
    uploader = models.CharField(max_length=30, null=False, blank=False)
    uploaded_date = models.CharField(max_length=30, null=False, blank=False , default = 'date')
    file_id = models.IntegerField(default='0')

    def __str__(self):
        return self.file_name

class ActivityLogs(models.Model):
    user = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    file_name = models.CharField(max_length=30, null=True, blank=True)
    file_type = models.CharField(max_length=30, null=True, blank=True , default = 'file')
    log_date = models.CharField(max_length=35, null=False, blank=False , default = 'date')

    def __str__(self):
        return self.user
