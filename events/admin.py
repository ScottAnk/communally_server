from django.contrib import admin

from .models import Event, Post, Tag

admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Tag)
