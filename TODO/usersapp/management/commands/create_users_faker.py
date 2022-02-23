from django.core.management.base import BaseCommand
import factory

from usersapp.models import User


class UsersFabric(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%s' % (n + 1))
    first_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    birthday_year = factory.Faker('year')
    password = '1234'


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()

        # При использовании UsersFabric.create_batch(10) в БД пароли
        # записываются в открытом виде, поэтому использовал немного другой метод
        # UsersFabric.create_batch(10)

        users = factory.build_batch(dict, size=10, FACTORY_CLASS=UsersFabric)
        for user in users:
            User.objects.create_user(**user)

        # Отдельно создадим суперпользователя
        User.objects.create_superuser(
            username='django',
            email='django@geekshop.local',
            password='geekbrains',
            birthday_year='1988'
        )
