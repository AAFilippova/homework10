from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BlogUser
class OtusUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogUser, UserAdmin)