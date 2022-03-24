from uuid import uuid4

from django.db import models

from usersapp.models import User


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(
        verbose_name='Назавание проекта',
        max_length=150,
    )
    url_on_repo = models.URLField(verbose_name='Ссылка на репозиторий',
                                  blank=True)
    users = models.ManyToManyField(User, verbose_name='Участиники проекта')

    def __str__(self):
        return f'{self.name}'


# Поле status сделаем максимальной длиной = 3, так как в дальнейшем возможно
# статусов будет больше.
class ToDo(models.Model):
    ACTIVE = 'A'
    CLOSE = 'C'

    STATUS_CHOICES = (
        (ACTIVE, 'Активна'),
        (CLOSE, 'Закрыта')
    )

    uid = models.UUIDField(primary_key=True, default=uuid4)
    name_todo = models.CharField(
        verbose_name='Назавание заметки',
        max_length=150,
    )
    project = models.ForeignKey(
        Project,
        verbose_name='Название проекта',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name='Текст')
    create_data = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    update_data = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=3,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )

    def delete(self, using=None, keep_parents=False):
        self.status = self.CLOSE
        self.save()
