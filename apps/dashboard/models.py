from django.db import models
from django.conf import settings


# Create your models here.
class FieldOfStudy( models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "Пользователь: ")

    title = models.CharField( max_length = 70, verbose_name = "Название направления:" )

    description = models.TextField( blank = True,  verbose_name = "Описание направления:" )

    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title