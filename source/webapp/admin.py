from django.contrib import admin
from .models import Guestbook


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_date', 'redacted_date')
    fields = ['name', 'email', 'status', 'text']
    list_filter = ('status',)
    search_fields = ('name',)


admin.site.register(Guestbook, GuestAdmin)
