import json
from django.core.management.base import BaseCommand

from usersapp.models import User


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('usersapp/json/users.json')
        User.objects.all().delete()
        for user in users:
            User.objects.create_user(**user)

        # Отдельно создадим суперпользователя
        User.objects.create_superuser(
            username='django',
            email='django@geekshop.local',
            password='geekbrains',
            birthday_year='1988'
        )
