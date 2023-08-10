from rest_framework import status
from rest_framework.test import APITestCase

from Lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        """Общие данные"""

        self.user = User.objects.create(email='3@admin.ru', password='spartak67', is_active=True)
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Создание урока тест"""
        data = {
            "lesson_name": "9",
            "lesson_description": "провекка валидации",
            "lesson_video_url": "youtube.com/jjj"
        }

        response = self.client.post('/lesson/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # status code
        self.assertTrue(Lesson.objects.all().exists()) # нахождение в базе
