from django.contrib import admin
from core.models import Requester

class RequesterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Requester, RequesterAdmin)
