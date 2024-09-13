from django.urls import path

from .views import (
    AuthorsIndexView,
    CreateCategory,
    ListCategory,
    UpdateCategory,
    UpdateArticle,
    ReadArticle,
    CreateArticle,
    ListArticle,
)
app_name = "animalblog_app"

urlpatterns = [
    path("article/create/", CreateArticle.as_view(), name="create_article"),
    path("authors/", AuthorsIndexView.as_view(), name="authors_index"),
    path("blog_animal_category/create/", CreateCategory.as_view(), name="create_category"),
    path("blog_animal_category/", ListCategory.as_view(), name="list_category"),
    path("blog_animal_category/update/<int:pk>/", UpdateCategory.as_view(), name="update_category"),
    path("product_category/", ListArticle.as_view(), name="list_article"),
    path("article/<int:pk>/", ReadArticle.as_view(), name="read_article"),
    path("article/update/<int:pk>/", UpdateArticle.as_view(), name="update_article"),
]