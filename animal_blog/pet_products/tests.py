from django.test import TestCase

from .models import ProductCategory, Product


class ProductsTest(TestCase):
    fixtures = [
        'product_category.json',
        'animal_category.json',
        'product.json'
    ]

    def test_product_category_count(self):
        self.assertGreater(ProductCategory.objects.count(), 0)

    def test_orders_login_required(self):
        response = self.client.get('/pet_products/orders/')
        self.assertEqual(302, response.status_code)

    def test_products_required(self):
        response = self.client.get('/pet_products/products/')
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(response.context['product_list']), 0)

    def test_product_association(self):
        product = Product.objects.get(title='Bone')
        category = ProductCategory.objects.get(name='Nutrition')
        self.assertEqual(product.product_category, category)