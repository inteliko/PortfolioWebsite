# admin.py

from django.contrib import admin
from .models import Contact, About

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
