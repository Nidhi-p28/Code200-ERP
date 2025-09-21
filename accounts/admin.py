from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, College

class UserAdmin(BaseUserAdmin):
    list_display = ("email", "full_name", "is_staff", "is_superuser")
    search_fields = ("email", "full_name")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name", "mobile_number", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "mobile_number", "role", "password1", "password2"),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(College)