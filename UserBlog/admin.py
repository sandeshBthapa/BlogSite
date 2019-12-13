from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


admin.site.register(Comment, CommentAdmin)
