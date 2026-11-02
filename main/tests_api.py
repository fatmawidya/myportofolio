import uuid
from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from main.models import Education, Experience


class PortfolioAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser('owner', 'owner@example.com', 'test-password')
        self.reader = User.objects.create_user('reader', password='test-password')
        self.editor = User.objects.create_user('editor', password='test-password')
        self.editor.groups.add(Group.objects.create(name='Editor'))
        self.payloads = {
            'experience': {'title': 'Portfolio', 'description': 'My work', 'category': 'volunteer',
                           'started_at': '2026-01-01T00:00:00Z', 'ended_at': None, 'thumbnail': ''},
            'education': {'institution': 'Universitas Indonesia', 'degree': 'bachelor',
                          'field_of_study': 'Information Systems', 'description': 'My studies',
                          'start_year': 2025, 'end_year': None, 'thumbnail': ''},
        }
        self.models = {'experience': Experience, 'education': Education}
        self.objects = {kind: self.models[kind].objects.create(**payload)
                        for kind, payload in self.payloads.items()}

    def url(self, kind, action='list', pk=None):
        return reverse(f'api:{kind}-{action}', args=[pk or self.objects[kind].pk] if action != 'list' else [])

    def test_public_read_search_and_missing(self):
        for kind in self.models:
            with self.subTest(kind=kind):
                result = self.client.get(self.url(kind)).data
                self.assertEqual(result[0]['id'], str(self.objects[kind].pk))
                self.assertFalse(result[0]['is_starred'])
                self.assertEqual(result[0]['star_count'], 0)
                self.assertNotIn('fields', result[0])
                self.assertNotIn('starred_by', result[0])
                self.assertNotIn('email', result[0])
                self.assertEqual(self.client.get(self.url(kind, 'detail')).status_code, 200)
                query = 'PORT' if kind == 'experience' else 'INFORMATION'
                self.assertEqual(len(self.client.get(self.url(kind), {'search': query}).data), 1)
                self.assertEqual(self.client.get(self.url(kind), {'search': 'missing'}).data, [])
                self.assertEqual(self.client.get(self.url(kind, 'detail', uuid.uuid4())).status_code, 404)

    def test_guest_and_reader_cannot_write_database(self):
        for user in [None, self.reader]:
            self.client.force_authenticate(user=user)
            for kind, model in self.models.items():
                with self.subTest(user=user, kind=kind):
                    self.assertEqual(self.client.post(self.url(kind), self.payloads[kind], format='json').status_code, 403)
                    self.assertEqual(self.client.patch(self.url(kind, 'detail'), {'description': 'forged'}, format='json').status_code, 403)
                    self.assertEqual(self.client.put(self.url(kind, 'detail'), self.payloads[kind], format='json').status_code, 403)
                    self.assertEqual(self.client.delete(self.url(kind, 'detail')).status_code, 403)
                    self.assertEqual(model.objects.count(), 1)
                    self.objects[kind].refresh_from_db()
                    self.assertEqual(self.objects[kind].description, self.payloads[kind]['description'])

    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.client.force_authenticate(self.editor)
        for kind, model in self.models.items():
            self.assertEqual(self.client.post(self.url(kind), self.payloads[kind], format='json').status_code, 403)
            self.assertEqual(self.client.delete(self.url(kind, 'detail')).status_code, 403)
            self.assertEqual(model.objects.count(), 1)
            self.assertEqual(self.client.patch(self.url(kind, 'detail'), {'description': 'Edited'}, format='json').status_code, 200)
            self.objects[kind].refresh_from_db()
            self.assertEqual(self.objects[kind].description, 'Edited')
            self.assertEqual(self.client.put(self.url(kind, 'detail'), self.payloads[kind], format='json').status_code, 200)

    def test_staff_without_editor_role_cannot_manage_data(self):
        self.reader.is_staff = True
        self.reader.save()
        self.client.force_authenticate(self.reader)
        for kind, model in self.models.items():
            self.assertEqual(self.client.post(self.url(kind), self.payloads[kind], format='json').status_code, 403)
            self.assertEqual(self.client.patch(self.url(kind, 'detail'), {'description': 'Forbidden'}, format='json').status_code, 403)
            self.assertEqual(self.client.delete(self.url(kind, 'detail')).status_code, 403)
            self.objects[kind].refresh_from_db()
            self.assertEqual(self.objects[kind].description, self.payloads[kind]['description'])
            self.assertEqual(model.objects.count(), 1)

    def test_editor_legacy_views_and_buttons_match_api_permissions(self):
        self.client.force_login(self.editor)
        for kind in self.models:
            edit_url = reverse(f'main:edit_{kind}', args=[self.objects[kind].pk])
            self.assertEqual(self.client.get(edit_url).status_code, 200)
            page = self.client.get(reverse(f'main:show_{kind}'))
            self.assertContains(page, 'const editHtml = (IS_SUPERUSER || IS_EDITOR)')
            self.assertContains(page, 'const deleteHtml = IS_SUPERUSER')

    def test_owner_create_put_patch_delete_and_readonly_fields(self):
        self.client.force_authenticate(self.owner)
        for kind, model in self.models.items():
            result = self.client.post(self.url(kind), {**self.payloads[kind], 'star_count': 99,
                'is_starred': True, 'starred_by': [self.reader.pk]}, format='json')
            self.assertEqual(result.status_code, 201)
            self.assertEqual(result.data['star_count'], 0)
            self.assertFalse(result.data['is_starred'])
            obj = model.objects.get(pk=result.data['id'])
            self.assertEqual(obj.starred_by.count(), 0)
            url = self.url(kind, 'detail', obj.pk)
            self.assertEqual(self.client.put(url, {'description': 'Incomplete'}, format='json').status_code, 400)
            self.assertEqual(self.client.put(url, self.payloads[kind], format='json').status_code, 200)
            self.assertEqual(self.client.patch(url, {'description': '<b>Clean</b>'}, format='json').status_code, 200)
            obj.refresh_from_db()
            self.assertEqual(obj.description, 'Clean')
            result = self.client.delete(url)
            self.assertEqual(result.status_code, 204)
            self.assertEqual(result.content, b'')
            self.assertFalse(model.objects.filter(pk=obj.pk).exists())

    def test_validation_and_no_invalid_writes(self):
        self.client.force_authenticate(self.owner)
        for kind, model in self.models.items():
            title = 'title' if kind == 'experience' else 'institution'
            for changes in [{title: '   '}, {title: '<img src=x>'}, {'description': '<b></b>'},
                            {'thumbnail': 'javascript:alert(1)'}]:
                self.assertEqual(self.client.post(self.url(kind), {**self.payloads[kind], **changes}, format='json').status_code, 400)
                self.assertEqual(model.objects.count(), 1)
            invalid_end = {'ended_at': '2020-01-01T00:00:00Z'} if kind == 'experience' else {'end_year': 2020}
            self.assertEqual(self.client.patch(self.url(kind, 'detail'), invalid_end, format='json').status_code, 400)
            self.objects[kind].refresh_from_db()
            self.assertEqual(self.objects[kind].description, self.payloads[kind]['description'])

    def test_star_uses_session_user_and_toggles(self):
        for kind in self.models:
            url = self.url(kind, 'star')
            self.client.force_authenticate(user=None)
            self.assertEqual(self.client.post(url).status_code, 403)
            self.assertEqual(self.objects[kind].starred_by.count(), 0)
            for user in [self.reader, self.editor, self.owner]:
                self.client.force_authenticate(user)
                result = self.client.post(url, {'user': self.owner.pk}, format='json')
                self.assertEqual(result.status_code, 200)
                self.assertTrue(result.data['is_starred'])
                self.assertEqual(result.data['star_count'], 1)
                self.assertEqual(list(self.objects[kind].starred_by.all()), [user])
                result = self.client.post(url)
                self.assertFalse(result.data['is_starred'])
                self.assertEqual(result.data['star_count'], 0)

    def test_wrong_method_and_browsable_api(self):
        self.client.force_authenticate(self.owner)
        for kind in self.models:
            self.assertEqual(self.client.delete(self.url(kind)).status_code, 405)
            self.assertEqual(self.client.get(self.url(kind, 'star')).status_code, 405)
            self.assertEqual(self.client.get(self.url(kind), HTTP_ACCEPT='text/html').status_code, 200)

    def test_head_and_options_do_not_change_data(self):
        for kind, model in self.models.items():
            for action in ['list', 'detail']:
                response = self.client.head(self.url(kind, action))
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content, b'')
                self.assertEqual(self.client.options(self.url(kind, action)).status_code, 200)
            self.assertEqual(model.objects.count(), 1)
            self.assertEqual(self.objects[kind].starred_by.count(), 0)

    def test_browsable_api_login_page(self):
        self.assertEqual(self.client.get(reverse('rest_framework:login')).status_code, 200)

    def test_session_csrf_rejection_and_success(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username='owner', password='test-password'))
        for kind, model in self.models.items():
            self.assertEqual(client.post(self.url(kind), self.payloads[kind], format='json').status_code, 403)
            self.assertEqual(model.objects.count(), 1)
            client.get(reverse(f'main:show_{kind}'))
            token = client.cookies['csrftoken'].value
            result = client.post(self.url(kind), self.payloads[kind], format='json', HTTP_X_CSRFTOKEN=token)
            self.assertEqual(result.status_code, 201)
            self.assertEqual(model.objects.count(), 2)

    def test_legacy_form_pages_share_templates_and_preserve_dates(self):
        self.client.force_login(self.owner)
        for kind in self.models:
            for action in ['create', 'edit']:
                url = reverse(f'main:{action}_{kind}', args=[self.objects[kind].pk] if action == 'edit' else [])
                page = self.client.get(url)
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, f'{kind}_form.html')
                if kind == 'experience' and action == 'edit':
                    self.assertContains(page, 'value="2026-01-01"')
