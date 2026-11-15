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

    def __str__(self):

        return self.title


class Topic(models.Model):
    field_of_study = models.ForeignKey(
        FieldOfStudy,
        on_delete=models.CASCADE,
        related_name='topics',
        verbose_name='Направление',
    )
    title = models.CharField(max_length=120, verbose_name='Тема')
    is_completed = models.BooleanField(default=False, verbose_name='Изучена')
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title
