from django.contrib import admin
from new.models import UserProfile
# Register your models here.
admin.site.register(UserProfile)

admin.site.site_header = 'Njana Njann'

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','user_info']

    def user_info(self,):
        return obj.description
