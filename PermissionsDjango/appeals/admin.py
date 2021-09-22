from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from .models import Appeal

# Register your models here.
admin.site.register(Appeal)

class AppealAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        'last_name',
        'email',
        'age',
        'education',
        'about',
        'appeal_date'
        'status',
        'department'
        'company',
        'about',
        'appeal_date',
        'cv',
    ]
    list_display_links=[
        'name',
    ]
    list_filter=[
        'department'
    ]
    search_fields=[
        'name'
    ]
    def __str__(self):
        return self.name
    class Meta:
        model = Appeal