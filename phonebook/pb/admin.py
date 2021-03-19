from django.contrib import admin

from .models import Contact, ContactInfo
# Register your models here.

admin.site.register(ContactInfo)
admin.site.register(Contact)