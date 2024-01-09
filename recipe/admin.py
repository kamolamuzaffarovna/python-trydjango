from django.contrib import admin
from .models import (
    Tag,
    Recipe,
    Ingredient
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


class IngredientAdminTabularInline(admin.TabularInline):
    model = Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAdminTabularInline,)
    list_display = ("id", "title", "description", "author", "created_date")
    search_fields = ("title", "author__username")
    list_filter = ("created_date",)
    autocomplete_fields = ("author",)
    data_hierarchy = 'created_date'
    filter_horizontal = ("tags",)
    readonly_fields = ("slug", "created_date")

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe", "title", "quantity", "unit", "is_active")
    search_fields = ("recipe_title", "title")
    list_filter = ("is_active", "unit")
    autocomplete_fields = ("recipe",)




