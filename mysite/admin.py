from django.contrib import admin
from .models import *

class leadAdmin (admin.ModelAdmin):
    list_display = ["name", "phone"]
    search_fields = ["name", "phone"]

    class Meta:
        model = lead

admin.site.register(lead, leadAdmin)
admin.site.register(uinfo)
# Register your models here.
