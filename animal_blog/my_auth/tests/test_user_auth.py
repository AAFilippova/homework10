from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from my_auth.forms import BlogUserCreateForm


class BlogUserRegisterTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            'username': 'admin',
            'email': 'admin@admin.local',
            'password1': 'MyP@ssw0rd',
            'password2': 'MyP@ssw0rd',
        }
        cls.user_broken_data = {
            'username': 'admin',
            'email': 'admin@admin.local',
            'password1': 'MyP@ssw0rd',
            'password2': 'min',
        }

    def tearDown(self):
        get_user_model().objects.all().delete()

    def test_succ_register(self):
        response = self.client.get(
            '/auth/register/',
        )
        self.assertContains(response, 'Username:', status_code=200)


        # # post
        response = self.client.post(
            '/auth/register/',
            data=self.user_data,
        )
        print(response.content)
        self.assertEqual(302, response.status_code)

        # check user
        new_user = get_user_model().objects.get(
            username=self.user_data['username']
        )

        self.assertEqual(
            self.user_data['email'],
            new_user.email,
        )

    def test_fail_register(self):
        response = self.client.post(
            # reverse('my_auth:register'),
            '/auth/register/',
            data=self.user_broken_data,
        )
        self.assertEqual(200, response.status_code)

        self.assertFormError(
            response.context['form'],
            'password2',
            ['The two password fields didn’t match.']

        )