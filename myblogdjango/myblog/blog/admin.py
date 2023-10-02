from django.contrib import admin
from .models import Post, User, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ['created_on']
    search_fields = ['title', 'content']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'email', 'pk')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'post_id', 'content')


