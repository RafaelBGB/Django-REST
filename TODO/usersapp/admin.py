from django.contrib import admin

from usersapp.models import User


# Зарегистируем таблицы которые будет видны в админке.
admin.site.register(User)
