from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from rest_framework import status
from mixer.backend.django import mixer

from todoapp.views import ProjectModelViewSet
from todoapp.models import Project, ToDo
from usersapp.models import User


class TestProjectModelViewSet(TestCase):
    def test_get_list_for_anonim_user(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_for_superuser(self):
        client = APIClient()
        User.objects.create_superuser('admin', 'admin@admin.com',
                                      'admin', birthday_year=1900)
        client.login(username='admin', password='admin')
        response = client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_post_project_for_anonim_user(self):
        client = APIClient()
        response = client.post('/api/projects/', {'name': 'poject_1'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_project_for_superuser(self):
        client = APIClient()
        User.objects.create_superuser('admin', 'admin@admin.com',
                                      'admin', birthday_year=1900)
        client.login(username='admin', password='admin')
        response = client.post('/api/projects/', {'name': 'project_1'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_put_project_for_anonim_user(self):
        client = APIClient()
        project = mixer.blend(Project)
        response = client.put(
            f'/api/projects/{project.uid}/',
            {'name': 'project_1',
             'url_on_repo': 'https://github.com/ToDo/project_1.git',
             'users': project.users}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        new_project = Project.objects.get(uid=project.uid)
        self.assertNotEqual(new_project.name, 'project_1')

    def test_put_project_for_superuser(self):
        client = APIClient()
        User.objects.create_superuser('admin', 'admin@admin.com',
                                      'admin', birthday_year=1900)
        client.login(username='admin', password='admin')
        project = mixer.blend(Project)
        response = client.put(
            f'/api/projects/{project.uid}/',
            {'name': 'project_1',
             'url_on_repo': 'https://github.com/ToDo/project_1.git'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_project = Project.objects.get(uid=project.uid)
        self.assertEqual(new_project.name, 'project_1')
        self.assertEqual(new_project.url_on_repo,
                         'https://github.com/ToDo/project_1.git')
        self.assertEqual(new_project.users, project.users)
        client.logout()


class TestToDoModelViewSet(APITestCase):
    def test_get_list_for_anonim_user(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_for_superuser(self):
        User.objects.create_superuser('admin', 'admin@admin.com',
                                      'admin', birthday_year=1900)
        self.client.login(username='admin', password='admin')
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_post_for_anonim_user(self):
        response = self.client.post('/api/todo/', {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_for_superuser(self):
        todo_mixer = mixer.blend(ToDo)
        User.objects.create_superuser('admin', 'admin@admin.com',
                                      'admin', birthday_year=1900)
        self.client.login(username='admin', password='admin')
        response = self.client.post(
            '/api/todo/',
            {
                'name_todo': 'todo2',
                'project': todo_mixer.project.uid,
                'author': todo_mixer.author.uid,
                'text': todo_mixer.text,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_for_anonim_user(self):
        todo_mixer = mixer.blend(ToDo)
        response = self.client.put(f'/api/todo/{todo_mixer.uid}/', {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_for_superuser(self):
        todo_mixer = mixer.blend(ToDo)
        project = Project.objects.create(name='project1')
        author = User.objects.create(username='user1', birthday_year=1990,
                                     email='user1@example.org')
        User.objects.create_superuser('admin', 'admin@admin.com',
                                      'admin', birthday_year=1900)
        self.client.login(username='admin', password='admin')
        ToDo.objects.create(
            name_todo=todo_mixer.name_todo,
            project=project,
            author=author,
            text=todo_mixer.text,
        )
        response = self.client.put(
            f'/api/todo/{todo_mixer.uid}/',
            {
                'name_todo': 'todo2',
                'project': todo_mixer.project.uid,
                'author': todo_mixer.author.uid,
                'text': 'new text',
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_todo = ToDo.objects.get(uid=todo_mixer.uid)
        self.assertEqual(new_todo.name_todo, 'todo2')
        self.assertEqual(new_todo.text, 'new text')
