from rest_framework import status
from rest_framework.test import APITestCase

from Lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        """Общие данные"""

        self.user = User.objects.create(
            email="3@admin.ru", password="spartak67", is_active=True
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.lesson_test = Lesson.objects.create(
            id=2,
            lesson_name="Урок 1",
            lesson_description="Описание тестового урока",
        )

    def test_create_lesson(self):
        """Создание урока тест"""
        data = {
            "lesson_name": "9",
            "lesson_description": "провекка валидации",
            "lesson_video_url": "youtube.com/jjj",
        }

        response = self.client.post("/lesson/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # status code
        self.assertTrue(Lesson.objects.all().exists())  # нахождение в базе

    def test_list_lesson(self):
        """Вывод всех уроков тест"""
        response = self.client.get("/lesson/list/")

        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 2,
                    "lesson_name": "Урок 1",
                    "lesson_description": "Описание тестового урока",
                    "lesson_preview": None,
                    "lesson_video_url": None,
                    "course": None,
                    "owner": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

    def test_detail_lesson(self):
        """Тест вывода инфрмании об одном уроке"""
        response = self.client.get("/lesson/deteil/2/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        """Тест обновления урока"""
        data = {
            "id": 3,
            "lesson_name": "Урок 1",
            "lesson_description": "Описание тестового урока",
        }

        response = self.client.put("/lesson/update/2/", data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        """Тест удаления урока"""
        response = self.client.delete("/lesson/delete/2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
