from django.views.generic import TemplateView
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DetailView,
)

from animalblog_app.models import Article, Author
from . models import AnimalCategory
from .forms import AnimalCategoryCreateUpdateForm , ArticleCreateUpdateForm
from .mixins import PageTitleMixin

class AuthorsIndexView(TemplateView):
    template_name = "animalblog_app/authors_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(

            authors=(
                Author.objects.all()
            ),
        )
        return context

class CreateCategory(PageTitleMixin,CreateView):
    model = AnimalCategory
    #template_name = 'pet_products/animalcategory_form.html'
    form_class = AnimalCategoryCreateUpdateForm
    success_url = "/"
    page_title = "Create Category"
   # model = ProductCategory
   # fields = "__all__"

class ListCategory(PageTitleMixin,ListView):
    model = AnimalCategory
    paginate_by = 10

class UpdateCategory(PageTitleMixin,UpdateView):
    model = AnimalCategory
    #template_name = 'pet_products/animalcategory_form.html'
    form_class = AnimalCategoryCreateUpdateForm
    success_url = "/"
    page_title = "Update Category"


class CreateArticle(PageTitleMixin,CreateView):
    model = Article
    #template_name = 'pet_products/animalcategory_form.html'
    form_class = ArticleCreateUpdateForm
    success_url = "/"
    page_title = "Create Article"
   # model = ProductCategory
   # fields = "__all__"

class ListArticle(PageTitleMixin,ListView):
    model = Article
    paginate_by = 10
class UpdateArticle(PageTitleMixin,UpdateView):
    model = Article
    #template_name = 'pet_products/animalcategory_form.html'
    form_class = ArticleCreateUpdateForm
    success_url = "/"
    page_title = "Update Article"


class ReadArticle(PageTitleMixin, DetailView):
    model = Article
    page_title = 'Article update'