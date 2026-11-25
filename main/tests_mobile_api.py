from django.contrib.auth.models import User
from django.test import override_settings
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from main.models import Education


class EducationTokenAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser('mobile-owner', 'owner@example.com', 'test-password')
        self.reader = User.objects.create_user('mobile-reader', password='test-password')
        self.payload = {
            'institution': 'Universitas Indonesia', 'degree': 'bachelor',
            'field_of_study': 'Sistem Informasi', 'start_year': 2025,
            'end_year': None, 'thumbnail': '', 'description': 'Belajar Flutter',
        }
        self.url = '/api/v1/education/'

    def test_token_login_create_public_read_logout_and_revocation(self):
        self.assertEqual(self.client.get(self.url).status_code, 200)
        self.assertEqual(self.client.post(self.url, self.payload, format='json').status_code, 401)
        login = self.client.post('/api/v1/auth/token/', {
            'username': 'mobile-owner', 'password': 'test-password',
        }, format='json')
        self.assertEqual(login.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + login.data['token'])
        created = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(created.status_code, 201)
        self.assertTrue(created.data['is_current'])
        self.assertIsNone(created.data['end_year'])
        self.assertEqual(Education.objects.count(), 1)
        detail_url = self.url + created.data['id'] + '/'
        anonymous = APIClient()
        self.assertEqual(anonymous.get(detail_url).status_code, 200)
        self.assertEqual(anonymous.get(self.url).data[0]['institution'], self.payload['institution'])
        self.assertEqual(self.client.post('/api/v1/auth/logout/').status_code, 204)
        self.assertFalse(Token.objects.filter(user=self.owner).exists())
        self.assertEqual(self.client.post(self.url, self.payload, format='json').status_code, 401)
        self.assertEqual(Education.objects.count(), 1)

    def test_reader_token_and_invalid_data_cannot_create_entries(self):
        reader_token = Token.objects.create(user=self.reader)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + reader_token.key)
        self.assertEqual(self.client.post(self.url, self.payload, format='json').status_code, 403)
        owner_token = Token.objects.create(user=self.owner)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + owner_token.key)
        invalid = {**self.payload, 'end_year': 2020}
        self.assertEqual(self.client.post(self.url, invalid, format='json').status_code, 400)
        self.assertEqual(Education.objects.count(), 0)

    @override_settings(CORS_ALLOW_ALL_ORIGINS=True)
    def test_web_preflight_allows_token_and_json_headers(self):
        response = self.client.options(self.url,
            HTTP_ORIGIN='http://localhost:5000',
            HTTP_ACCESS_CONTROL_REQUEST_METHOD='POST',
            HTTP_ACCESS_CONTROL_REQUEST_HEADERS='authorization,content-type',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], '*')
        self.assertIn('authorization', response.headers['Access-Control-Allow-Headers'])
