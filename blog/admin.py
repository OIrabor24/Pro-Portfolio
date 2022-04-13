from django.contrib import admin
from blog.models import Category, Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'body', 'created_on', 'last_modified')

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('author', 'created_on', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Comment, CommentAdmin) 