from django.contrib import admin
from .models import Author, Comment, Post, Tag

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ('first_name', 'last_name', 'email',)
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date',)
    list_filter = ('tags', 'date', 'author',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    list_filter = ('caption',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'text',)
    list_filter = ('user_name',)
    
