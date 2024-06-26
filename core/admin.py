from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class CandResource(resources.ModelResource):
    class Meta:
        model = UserProfile
        fields = ('registration_number','name','fathername','mothername','email','phone','whatsapp','center__centername','medium','created_at')

class CandAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'phone', 'center')
    list_filter = ['center']
    resource_classes = [CandResource]


    
admin.site.register(Center)
admin.site.register(UserProfile,CandAdmin)
# Register your models here.
