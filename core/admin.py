from django.contrib import admin
from .models import Employee, Client

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.get_fields()]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.get_fields()]