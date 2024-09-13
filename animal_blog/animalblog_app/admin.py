import textwrap
from django.contrib import admin

#from shop_app.models import Category
from .models import AnimalCategory, Author, Article

class ShortDescriptionMixin:

    @classmethod
    def short_description(cls, obj: AnimalCategory) -> str:
        return textwrap.shorten(obj.description, width=50)


@admin.register(AnimalCategory)
class AnimalCategoryAdmin(admin.ModelAdmin, ShortDescriptionMixin):
    list_display = "pk", "name", "short_description" ,
    #  list_display = "pk","name", "short_description"
    list_display_links = "pk", "name"


@admin.register(Author)
class Author(admin.ModelAdmin, ShortDescriptionMixin):
    list_display = "pk", "username", "name", "short_description"
    #  list_display = "pk","name", "short_description"
    list_display_links = "pk", "username", "name"


@admin.register(Article)
class Article(admin.ModelAdmin, ShortDescriptionMixin):
    list_display = "pk", "title", "author","category",  "short_description"
    #  list_display = "pk","name", "short_description"
    list_display_links = "pk", "title"
