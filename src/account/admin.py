from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'username', 'is_active', 'avatar']


admin.site.register(User, UserAdmin)
