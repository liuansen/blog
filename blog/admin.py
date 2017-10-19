from django.contrib import admin
from .models import Post, CateGory, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(CateGory)
admin.site.register(Tag)

