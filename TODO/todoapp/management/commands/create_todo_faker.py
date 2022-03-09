from random import randint

from django.core.management.base import BaseCommand
import factory

from usersapp.models import User
from todoapp.models import Project, ToDo


class ProjectFabric(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: 'project%s' % (n + 1))
    url_on_repo = factory.LazyAttribute(
        lambda o: 'https://github.com/ToDo/%s.git' % o.name
    )

    # Так как у нас связь с пользователями "многие ко многим" используем
    # специальный декоратор, из-за использования данного декоратора мы не
    # сможем использовать метод create_batch() поэтому используем при создании
    # цикл for
    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.users.add(user)


class ToDoFabric(factory.django.DjangoModelFactory):
    class Meta:
        model = ToDo

    project = factory.SubFactory(ProjectFabric)
    text = factory.Faker('sentence', nb_words=20)


class Command(BaseCommand):
    def handle(self, *args, **options):
        Project.objects.all().delete()
        ToDo.objects.all().delete()

        for i in range(5):
            # Вытащим из базы всех пользователей кроме администратора "django",
            # отсортируем случайным образом (метод order_by('?')
            # сильно нагружает базу) и получим от 1 до 5 первых пользователй
            user_list = User.objects.exclude(username='django').order_by('?')[
                        :randint(1, 5)]
            ProjectFabric(users=user_list)

        project_list = Project.objects.all()

        for project in project_list:
            _ = randint(3, 10)
            for i in range(_):
                author = User.objects.exclude(username='django').order_by(
                    '?').first()
                ToDoFabric(project=project, author=author)
