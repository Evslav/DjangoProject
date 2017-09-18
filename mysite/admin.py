from django.contrib import admin
from .models import *

class leadAdmin (admin.ModelAdmin):
    list_display = ["name", "phone"]
    search_fields = ["name", "phone"]

    class Meta:
        model = lead
        model = uinfo

admin.site.register(lead, leadAdmin)

# Register your models here.
