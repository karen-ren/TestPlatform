from django.contrib import admin
from TestManagement.models.project import APIProject
from TestManagement.models.module import APIModule


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "create_time"]
    search_fields = ["name"]
    list_filter = ["status"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "create_time", "project"]
    search_fields = ["name"]
    list_filter = ["project"]


# Register your models here.
admin.site.register(APIProject, ProjectAdmin)
admin.site.register(APIModule, ModuleAdmin)


