from django.contrib import admin

from main_app.models import Choice, WouldYouRather

# Register your models here.
admin.site.register(WouldYouRather)
admin.site.register(Choice)