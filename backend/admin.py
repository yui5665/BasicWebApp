from django.contrib import admin
from .models import modelsList

# Register your models here.
for x in modelsList:
    admin.site.register(x)