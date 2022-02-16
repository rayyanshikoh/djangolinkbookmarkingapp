from django.contrib import admin
from django.utils.html import format_html

from . import models
# Register your models here.

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_link']
    list_per_page = 10
    list_filter = ['category']
    fields = ['title', 'link', 'description', 'category']
    autocomplete_fields = ['category']
    search_fields = ['title']
    def get_link(self, link):
        return format_html('<a href={}>{}</a>', link.link, link.title)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields= ['title']