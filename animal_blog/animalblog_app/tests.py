from django.test import TestCase

from .models import Author


class BlogTest(TestCase):

    fixtures = [
        'author.json',
        'article.json',
        'animal_category.json',
    ]
    def test_authors_qty(self):
        qty = Author.objects.count()
        self.assertEqual(qty, 3)

    def test_author_required(self):
        response = self.client.get('/animalblog/authors/')
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(response.context['authors']), 0)

    def test_article_detail(self):
        response = self.client.get('/animalblog/article/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['article'].id, 1)
        print(response.context.keys())
