from django.contrib import admin
from .models import Company

# Register your models here.
admin.site.register(Company)

class CompanyAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'content',
        'location',
        'image',
        'created_date',
    ]
    list_display_links=[
        'title',
    ]
    search_fields=[
        'title'
    ]
    list_filter = [
        'created_date'
    ]
    def __str__(self):
        return self.title
    class Meta:
        model = Company