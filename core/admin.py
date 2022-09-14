from django.contrib import admin

from .models import Commands, Devices, Intents

admin.site.register(Devices)
admin.site.register(Intents)
admin.site.register(Commands)
