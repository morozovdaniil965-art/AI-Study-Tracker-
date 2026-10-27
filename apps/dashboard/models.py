from django.db import models
from django.conf import settings


# Create your models here.
class FieldOfStudy( models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "Пользователь: ")

    title = models.CharField( max_length = 70, verbose_name = "Название направления:" )

    description = models.TextField( blank = True,  verbose_name = "Описание направления:" )

    image_user = models.ImageField( null = True, blank = True, upload_to='subject_icons/%Y/%m/%d', verbose_name = "Добавить иконку:")

    image_icon = models.CharField( blank = True, max_length=30, verbose_name = "Стандартная иконка:" )

    date_create = models.DateTimeField(auto_now_add=True)

    def clean(self):

        if self.image_user and self.image_icon:

            raise ('Ошибка')


    def __str__(self):

        return self.title