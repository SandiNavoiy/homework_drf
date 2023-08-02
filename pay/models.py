from django.db import models

from users.models import User


# Create your models here.
class Pay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    pay_date = models.DateField(verbose_name='дата платежа', auto_now=True)
