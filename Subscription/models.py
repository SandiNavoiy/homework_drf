from django.db import models

from config import settings
from Course.models import NULLABLE, Course


class Subscription(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        **NULLABLE,
        related_name="subscription",
        verbose_name="Подписка на курс",
    )
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Подписчик",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.course}:{self.subscriber}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
