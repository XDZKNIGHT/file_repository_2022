from django.contrib import admin

# Register your models here.
from .models import Profiles
from .models import UploadedFile
from .models import Archive
from .models import ArchiveFile
from .models import ActivityLogs

admin.site.register(Profiles)
admin.site.register(UploadedFile)
admin.site.register(Archive)
admin.site.register(ArchiveFile)
admin.site.register(ActivityLogs)