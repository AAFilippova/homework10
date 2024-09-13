from django.views.generic import CreateView

from .forms import BlogUserCreateForm
from .models import BlogUser


class BlogUserCreateView(CreateView):
    model = BlogUser
    success_url = '/'
    form_class = BlogUserCreateForm
