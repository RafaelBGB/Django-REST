from django.contrib import admin

from todoapp.models import Project, ToDo


admin.site.register([ToDo, Project])
