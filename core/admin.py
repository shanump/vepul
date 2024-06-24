from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class BookResource(resources.ModelResource):
    class Meta:
        model = UserProfile  # or 'core.Book'

class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]

admin.site.register(Center)
admin.site.register(UserProfile,BookAdmin)
# Register your models here.
