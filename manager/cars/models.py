from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    year = models.CharField('Год выпуска', null=True, blank=True, max_length=50)
    description = models.TextField('Описание', max_length=2500)
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    updated_at = models.DateTimeField('Дата обновления', default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} {self.model}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class CarComments(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'