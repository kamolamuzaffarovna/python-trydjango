from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'slug', 'create_date', 'modified_date')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('create_date', 'modified_date')

admin.site.register(Article, ArticleAdmin)
