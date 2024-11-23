from http import HTTPStatus

from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.github.provider import GitHubProvider
from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse

from users.models import User
# Create your tests here.

class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Дмитрий',
            'last_name': 'Пугач',
            'username': 'Pimple',
            'email': '07700660gg@mail.ru',
            'password1': 'Ratatyi.2020',
            'password2': 'Ratatyi.2020'
        }
        self.path = reverse('users:registration')

        self.social_app = SocialApp.objects.create(provider=GitHubProvider.id)

        site = Site.objects.get_current()
        self.social_app.sites.add(site)


    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())




