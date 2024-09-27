from django.contrib import admin
from .models import Blog , PropertyType , Search
# Register your models here.

admin.site.register(Blog)
admin.site.register(PropertyType)
admin.site.register(Search)