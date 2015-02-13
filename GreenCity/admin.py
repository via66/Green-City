from django.contrib import admin
from models import GreenProject

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
    ]

admin.site.register(GreenProject, ProjectAdmin)