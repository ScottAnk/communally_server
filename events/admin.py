from django.contrib import admin

from .models import Event, Post, User, Tag

admin.site.register(Event)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Tag)
