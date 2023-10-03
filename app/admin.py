from django.contrib import admin
from .models import Client, SuperuserProfile
from django.contrib.auth.models import Group

# Register your models here.
class ClietAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'installation', 'installation_type', 'installation_date', 'address', 'phone_number')
    list_filter = ['installation_type'] 

class SuperuserProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'permission']


admin.site.unregister(Group)
admin.site.register(Client, ClietAdmin)
admin.site.register(SuperuserProfile, SuperuserProfileAdmin)
