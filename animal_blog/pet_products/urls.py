from django.urls import path

from .views import (
    ListProducts,
    OrdersIndexView,
    task_status,
    #create_product_category
    CreateProductCategory,
    ListProductCategory,
    UpdateProductCategory,
    ReadProductCategory,

)

app_name = "pet_products"

urlpatterns = [
    path("products/", ListProducts.as_view(), name="products_index"),
    path("orders/", OrdersIndexView.as_view(), name="orders_index"),
    path("task_status/", task_status, name="task_status"),
    #path("product_category/create/", create_product_category, name="create_product_category"),
    path("product_category/create/", CreateProductCategory.as_view(), name="create_product_category"),
    path("product_category/", ListProductCategory.as_view(), name="list_product_category"),

    path("product_category/<int:pk>/", ReadProductCategory.as_view(), name="read_product_category"),
    path("product_category/update/<int:pk>/", UpdateProductCategory.as_view(), name="update_product_category"),

]