from rest_framework import status
from rest_framework.test import APITestCase

from Course.models import Course
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        """Общие данные"""

        self.user = User.objects.create(email='3@admin.ru', password='spartak67', is_active=True)
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course_test = Course.objects.create(
            course_name='Эскимосский язык',
            course_description='ТЭскимосский язык',
        )

    def test_create_course(self):
            """Создание курса тест"""
            data = {

        "course_name": "латинский",
        "course_description": "латинский язык "

    }

            response = self.client.post('/course/course/', data=data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(Course.objects.all().exists())  # нахождение в базе

    def test_list_course(self):
        """Вывод всех курсов"""
        response = self.client.get('/course/course/')

        data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': 3,
                 'course_name': 'Эскимосский язык',
                 'lessons_count': 0,
                 'lessons': None,
                 'subscription': False,
                 'course_description': 'ТЭскимосский язык',
                 'course_preview': None,
                 'owner': None}

            ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            data
        )


