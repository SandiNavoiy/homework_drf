from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name="название курса")
    course_description = models.TextField(verbose_name="описание курса", **NULLABLE)
    course_preview = models.ImageField(
        upload_to="course/", verbose_name="изображение", **NULLABLE
    )

    def __str__(self):
        return f"{self.course_name} {self.course_description}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
