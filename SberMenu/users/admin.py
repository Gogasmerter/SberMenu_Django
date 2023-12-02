from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "first_name", "last_name", "is_active")
    list_filter = ("email", "is_staff", "is_superuser", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "user_permissions")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)
    readonly_fields = (
        User.date_joined.field.name,
        User.last_login.field.name,
    )


admin.site.register(User, UserAdmin)
