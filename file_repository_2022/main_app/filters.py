from dataclasses import field
import django_filters
from .models import UploadedFile, ArchiveFile, ActivityLogs
from django_filters import DateFilter


class AdminFileFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='uploaded_date',
                            lookup_expr='icontains')

    class Meta:
        model = UploadedFile
        fields = {
            'file_name': ['icontains'],
            'file_type': ['icontains'],
            'uploader': ['icontains'],
        }
        exclude = ['file', 'uploaded_date']

class AdminArchiveFileFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='uploaded_date',
                            lookup_expr='icontains')

    class Meta:
        model = ArchiveFile
        fields = {
            'file_name': ['icontains'],
            'file_type': ['icontains'],
            'uploader': ['icontains'],
        }
        exclude = ['file', 'uploaded_date']


class UserFileFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='uploaded_date',
                            lookup_expr='icontains')

    class Meta:
        model = UploadedFile
        fields = {
            'file_name': ['icontains'],
            'file_type': ['icontains'],
        }
        exclude = ['file', 'uploaded_date', 'uploader']

class UserArchiveFileFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='uploaded_date',
                            lookup_expr='icontains')

    class Meta:
        model = ArchiveFile
        fields = {
            'file_name': ['icontains'],
            'file_type': ['icontains'],
        }
        exclude = ['file', 'uploaded_date', 'uploader']

class ActivityLogFileFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='log_date',
                            lookup_expr='icontains')

    class Meta:
        model = ActivityLogs
        fields = {
            'user': ['icontains'],
            'file_name': ['icontains'],
            'file_type': ['icontains'],
        }
        exclude = ['file', 'log_date']