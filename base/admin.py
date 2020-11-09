from django.contrib import admin
from .models import Post, Tag, PostImg
    
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(PostImg)