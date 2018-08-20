from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class CategoryAdmin(admin.ModelAdmin):
	exclude = ('posts', )

class CategoryInLine(admin.TabularInline):
	model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
	inline = [
		CategoryInLine,
	]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
