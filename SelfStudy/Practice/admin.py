from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin


# Register your models here.

class DepartmentAdmin(SimpleHistoryAdmin):
    pass


class UserAdmin(SimpleHistoryAdmin):
    list_display = ['first_name', 'last_name', 'department']
    list_filter = ['first_name', 'last_name', 'department']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(User, UserAdmin)
