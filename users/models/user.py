from django.db import models

from users.models.location import Location


class User(models.Model):
    ROLES = [
        ('admin', 'Администратор'),
        ('member', 'Пользователь'),
        ('moderator', 'Модератор')
    ]

    first_name = models.CharField(verbose_name="Имя", max_length=100, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, null=True)
    username = models.CharField(verbose_name="Логин", max_length=20, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=200)
    role = models.CharField(max_length=10, choices=ROLES, default='member')
    age = models.SmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.username
