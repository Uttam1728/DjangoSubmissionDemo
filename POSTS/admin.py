from django.contrib import admin

from POSTS.models import Post, Attachment

# Register your models here.

admin.site.register(Post)
admin.site.register(Attachment)
