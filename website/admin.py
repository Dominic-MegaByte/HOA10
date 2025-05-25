from django.contrib import admin

from django.contrib import admin

from .models import Sign

class SignAdmin(admin.ModelAdmin):
    list_display = ('name', 'months', 'element', 'symbol', 'nickname', 'compatibility', 'personalities', 'weakness', 'modalities')

admin.site.register(Sign, SignAdmin)

