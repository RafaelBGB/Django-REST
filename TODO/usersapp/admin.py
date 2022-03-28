from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usersapp.models import User


# Зарегистируем таблицы которые будет видны в админке.
admin.site.register(User, UserAdmin)
