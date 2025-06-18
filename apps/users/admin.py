from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_email_verified', 'signup_source', 'onboarding_complete')
    search_fields = ('email', 'username')
