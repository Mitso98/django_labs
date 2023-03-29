from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)  # To show post and it's comments
admin.site.register(Comment)


# # Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
