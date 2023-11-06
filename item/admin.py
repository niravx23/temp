from django.contrib import admin

from .models import Category, Item


@admin.register(Item)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name" , "price" , "created_at" , "created_by"]
    list_filter = ["price"]
    
@admin.register(Category)
class PersonAdminForCategory(admin.ModelAdmin):

    list_display = ["name" ]
  