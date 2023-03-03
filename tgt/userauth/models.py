from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import uuid


class Department(models.Model):
    department = models.CharField('Отдел', max_length=50)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.department


class CustomUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    phone_number_work = models.CharField('Рабочий телефон', max_length=16, blank=True, null=True)
    phone_number_mobile = models.CharField('Мобильный телефон', max_length=12, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Отдел')

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + " " + self.last_name


