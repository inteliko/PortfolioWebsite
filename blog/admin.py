from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category, Comment

class CommentAdmin(admin.ModelAdmin):
 list_display = ('post', 'name', 'email', 'content', 'created_at', 'ip_address')
class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;"/>'.format(obj.image.url))

    display_image.allow_tags = True
    display_image.short_description = 'Image Preview'

    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
