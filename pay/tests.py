from rest_framework import status
from rest_framework.test import APITestCase

from pay.models import Pay
from users.models import User


class PayTestCase(APITestCase):
    def setUp(self) -> None:
        """Общие данные"""

        self.user = User.objects.create(email='3@admin.ru', password='spartak67', is_active=True)
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.lesson_test = Pay.objects.create(
            id=2,
            pay_date='2099-08-06"',
            pay_sum=15,
            payment_type="CASH",
            user=self.user

        )

    def test_create_pay(self):
        """Создание курса тест"""

        data = {

            "pay_date": "2023-08-06",
            "pay_sum": 154545420,
            "payment_type": "CASH",
            "user": self.user.id
        }

        response = self.client.post('/pay/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Pay.objects.all().exists())  # нахождение в базе

    def test_list_pay(self):
        """Вывод всех оплат тест"""
        responce = self.client.get('/pay/list/')
        print(responce.json())
        print("+++++++++++++++++++++++++++")
        data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': 2,
                 'pay_date': '2023-08-11',
                 'pay_sum': 15,
                 'payment_type': 'CASH',
                 'user': 1,
                 'course_name': None,
                 'lesson_name': None}

            ]
        }

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(
            responce.json(),
            data

        )
