from django.db import models
from django.utils import timezone

class action(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата подачи заявки')
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')
    text = models.TextField(blank = True, verbose_name='Текст')
    finished = models.BooleanField(default = False, verbose_name='Выполнено')
    class Meta:
        ordering = ['finished', '-created_date']
    def __str__(self):
        return self.name
class purchase(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')
    text = models.TextField(blank = True, verbose_name='Текст')
    finished = models.BooleanField(default = False, verbose_name='Выполнено')
    class Meta:
        ordering = ['finished', '-created_date']
    def __str__(self):
        return self.name
class knowledge(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')
    text = models.TextField(blank = True, verbose_name='Текст')
    finished = models.BooleanField(default = False, verbose_name='Выполнено')
    class Meta:
        ordering = ['finished', '-created_date']
    def __str__(self):
        return self.name
class tracking_number(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания/建立日期')
    name = models.CharField(max_length=128, blank=False, verbose_name='Номер трека/快递单号码')
    text = models.TextField(blank = True, verbose_name='Описание/简介')
    finished = models.BooleanField(default = False, verbose_name='Получено в Китае/在中国收到')
    finished1 = models.BooleanField(default = False, verbose_name='Получено за рубежом/在国外收到')
    class Meta:
        ordering = ['-created_date','finished']
    def __str__(self):
        return self.name


# Create your models here.
