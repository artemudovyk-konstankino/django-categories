from django.contrib import admin

from django_categories.admin import CategoryBaseAdmin

from .models import SimpleCategory


class SimpleCategoryAdmin(CategoryBaseAdmin):
    pass


admin.site.register(SimpleCategory, SimpleCategoryAdmin)
