from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ('name',)
    }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ('title',)
    }
    ...