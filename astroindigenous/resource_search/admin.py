from django.contrib import admin

# Register your models here.
from .models import Resource, Tag

admin.site.register(Resource)
admin.site.register(Tag)
