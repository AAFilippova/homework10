from django import forms
from django.forms import ModelForm

from .models import ProductCategory


class ProductCategoryCreateUpdateForm(ModelForm):
    # commit = forms.BooleanField(widget=)
    class Meta:
        model = ProductCategory
        fields = '__all__'
        # fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            # field: forms.Field
            # widget: forms.Widget = field.widget
            field.widget.attrs["class"] = "form-control"
            # field.help_text = 'hello'
            # if isinstance(field, forms.CharField):
            #     print(field.label, type(field.label))

    def clean_name(self):
        name = self.cleaned_data['name']
        print('name:', name)

        if name.islower():
            raise forms.ValidationError('only Capital name')

        return name