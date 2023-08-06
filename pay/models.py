from django.db import models

from Course.models import NULLABLE, Course
from Lesson.models import Lesson
from users.models import User


# Create your models here.
class Pay(models.Model):
    CHOICES = (
        ('Card', 'карта'),
        ('CASH', 'наличка'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    pay_date = models.DateField(verbose_name='дата платежа', auto_now=True)
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE)
    lesson_name = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE)
    pay_sum  = models.IntegerField(verbose_name='сумма платежа')
    payment_type = models.CharField(choices=CHOICES, verbose_name='тип оплаты')


    def __str__(self):
        return f'{self.user} {self.course_name}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
