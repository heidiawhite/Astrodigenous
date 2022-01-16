from django.contrib import admin

# Register your models here.
from .models import Resource, Tag, Language, Format

admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Language)
admin.site.register(Format)
