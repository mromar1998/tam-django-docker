from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(PhoneNumber)
admin.site.register(Contact)
admin.site.register(Name)
