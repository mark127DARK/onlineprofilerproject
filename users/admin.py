from django.contrib import admin
from .models import User 
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

admin.site.site_header = "Profiler Web App Admin"
admin.site.title_header = "Profiler Admin"
admin.site.index_title = "Welcome to Our Online Web App Profilers"

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'image_tag',
        'user_position',
        'date_filled_up',
        'user_lname',
        'user_fname',
        'user_mi',
        'date_of_birth',
        'user_area',
        'user_training',
        'user_venue'
    ]
    
admin.site.register(User, UserAdmin)
