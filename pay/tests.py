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
        self.pay_test = Pay.objects.create(
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

        data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': 2,
                 'pay_date': '2023-08-11',
                 'pay_sum': 15,
                 'payment_type': 'CASH',
                 'user': self.user.id,
                 'course_name': None,
                 'lesson_name': None}

            ]
        }

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(
            responce.json(),
            data

        )

    def test_detail_pay(self):
        """Вывод одной оплаты тест"""
        response = self.client.get('/pay/deteil/2/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_pay(self):
        data = {

            'pay_sum': 150,
            'pay_date': '2023-08-12',
            'payment_type': 'CASH',
            'user': self.user.id
        }

        response = self.client.put('/pay/update/2/', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

    def test_delete_pay(self):
        response = self.client.delete('/pay/delete/2/')
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
