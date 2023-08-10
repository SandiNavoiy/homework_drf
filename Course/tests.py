from rest_framework.test import APITestCase

from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        """Общие данные"""

        self.user = User.objects.create(email='3@admin.ru', password='spartak67', is_active=True)
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
            """Создание курса тест"""
            pass


