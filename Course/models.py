from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name="название курса")
    course_description = models.TextField(verbose_name="описание курса", **NULLABLE)
    course_preview = models.ImageField(
        upload_to="course/", verbose_name="изображение", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )
    price = models.FloatField(default=1000.00, verbose_name="Цена USD")
    last_updated = models.DateTimeField(
        default=timezone.now, verbose_name="последнее обновление"
    )

    def __str__(self):
        return f"{self.course_name} {self.course_description}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
