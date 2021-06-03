from django.contrib import admin
from developers.models import *


class User_Admin(admin.ModelAdmin):
    list_display = ('uid', 'created_time')


class service_Admin(admin.ModelAdmin):
    list_display = ('uid', 'user_id', 'service', 'datetime')


admin.site.register(User, User_Admin)
admin.site.register(service, service_Admin)
