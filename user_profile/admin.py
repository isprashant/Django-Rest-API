from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User Info", {'fields': ['user', 'about', 'city', 'mobile']}),
        ('Verification', {'fields': ['driving_licence', 'pancard','is_driving_licence_verified',\
                                     'is_pancard_verified']})
    ]

    list_display = ['user','is_dl_verified', 'is_pc_verified', 'mobile']


admin.site.register(UserProfile, UserProfileAdmin)
