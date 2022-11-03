from django.db import models

# Create your models here.
class Person(models.Model):
    f_name = models.CharField(max_length=11, blank=False,verbose_name="Имя")
    l_name = models.CharField(max_length=21, blank=False,verbose_name="Фамилия")
