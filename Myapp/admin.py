from django.contrib import admin
from .models import Department, Project, Employee

# Register your models here
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Employee)
