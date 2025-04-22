from django.contrib import admin
from .models import category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(category)
admin.site.register(Blog, BlogAdmin)