from django.contrib import admin

# Register your models here.
from users.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_joined']
