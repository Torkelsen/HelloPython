from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    list_filter = ("date", "occupation")
    ordering = ("first_name", ) # "-" prefix will be descending sort
    readonly_fields = ("occupation", )

admin.site.register(Form, FormAdmin)
