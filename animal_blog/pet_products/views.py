from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    ListView,
    UpdateView,
)

from celery.result import AsyncResult

from pet_products.models import Product, Order, ProductCategory
from pet_products.forms import ProductCategoryCreateUpdateForm
from .mixins import PageTitleMixin

class ListProducts(PageTitleMixin,ListView):
    model = Product
    paginate_by = 10




class OrdersIndexView(LoginRequiredMixin,TemplateView):
    template_name = "pet_products/orders_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # orders=Order.objects.all(),
            # orders=Order.objects.prefetch_related("products").all(),
            # orders=Order.objects.prefetch_related("order_products").all(),
            # orders=Order.objects.prefetch_related("order_products__product").all(),
            # orders=Order.objects.select_related("user").all(),
            orders=(
                Order.objects.select_related("user")
                .prefetch_related("order_products__product")
                .all()
            ),
        )
        return context
def task_status(request: HttpRequest) -> HttpResponse:
    context = {}
    task_id =request.GET.get("task_id")
    if task_id is None:
        return HttpResponseBadRequest("Task ID is required")
    result = AsyncResult(id=task_id)
    is_ready = result.ready()
    status = result.status
    task_result = result.result
    context.update(
        task_id=task_id,
        is_ready=is_ready,
        status=status,
        result=task_result,
    )
    return render(
        request=request,
        template_name="pet_products/task_status.html",
        context=context,
    )

#def create_product_category(request):
#    if request.method == "POST":
#        form = ProductCategoryCreateUpdateForm(request.POST,request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("/")
#    else:
#        form = ProductCategoryCreateUpdateForm()
#
#    context = {"create_form": form,}
#
#    return render(request, 'pet_products/animalcategory_form.html', context)

class CreateProductCategory(PageTitleMixin,CreateView):
    model = ProductCategory
    #template_name = 'pet_products/animalcategory_form.html'
    form_class = ProductCategoryCreateUpdateForm
    success_url = "/"
    page_title = "Create Product Category"
   # model = ProductCategory
   # fields = "__all__"

class ListProductCategory(PageTitleMixin, PermissionRequiredMixin,ListView):
    model = ProductCategory
    paginate_by = 10
    permission_required = 'view_productcategory'

class UpdateProductCategory(PageTitleMixin,UpdateView):
    model = ProductCategory
    #template_name = 'pet_products/animalcategory_form.html'
    form_class = ProductCategoryCreateUpdateForm
    success_url = "/"
    page_title = "Update Product Category"

class ReadProductCategory(PageTitleMixin,DetailView):
    model = ProductCategory
    page_title = 'Product Category update'