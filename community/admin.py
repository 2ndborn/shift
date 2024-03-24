from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'image',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)