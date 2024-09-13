from django.contrib.auth.forms import UserCreationForm

from .models import BlogUser


class BlogUserCreateForm(UserCreationForm):
    class Meta:
        model = BlogUser
        fields = ('username', 'email', 'password1', 'password2')