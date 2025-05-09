from django.contrib import admin
from .models import table
from django.contrib import admin

from .models import Contact
admin.site.register(Contact)





@admin.register(table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'date',
        'time',
        'people',
        'purpose',
    )
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date', 'purpose', 'role')
