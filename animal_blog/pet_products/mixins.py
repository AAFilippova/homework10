from django.views.generic import CreateView

from pet_products.forms import ProductCategoryCreateUpdateForm


class PageTitleMixin:
    page_title = 'Animals'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_title'] = self.page_title
        return context