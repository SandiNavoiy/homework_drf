from rest_framework import serializers
import stripe
from Course.models import Course
from config import settings

stripe.api_key = settings.STRIPE_API_KEY

class CourseSerializer(serializers.ModelSerializer):
    # добавление поля количество уроков  через описание нового типа, и сслыкой на запрос к лесссон, суммирование
    lessons_count = serializers.IntegerField(
        source="lesson_set.all.count", read_only=True
    )
    # Добавление в сериализатор уроков для курса, смотри функцию get_lessons

    lessons = serializers.SerializerMethodField(read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)
    payments = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, instance):
        """Добавление уроков для курса"""
        lesson_list = []
        if instance.lesson_set.all():
            for i in instance.lesson_set.all().values_list():
                lesson_list.append(i[1])
            return lesson_list
        return None

    def get_subscription(self, instance):
        """Добавление подписки для курса"""
        request = self.context.get("request")
        user = request.user
        sub_all = instance.subscription.all()
        for sub in sub_all:
            if sub.subscriber == user:
                return True
        return False

    def get_url_payments(self, course):
        """Добавление оплаты для курса"""
        #создание продукта с именем, которое берется из имени курса ( course.course_name)
        payment = stripe.Product.create(name=course.course_name, )
        #Создание цены на продукт:
        price = stripe.Price.create(
            # сумма
            unit_amount=int(course.price),
            # валюта
            currency="usd",
            # привязка к продукту
            product=payment['id'],
        )
        #Создание платежной сессии
        session = stripe.checkout.Session.create(
            # адрес после успешного платежа
            success_url="https://example.com/success",
            line_items=[
                {
                    "price": price['id'],
                    # количество
                    "quantity": 1,
                },
            ],
            # Режим платежа,(что такое не понял)
            mode="payment",
        )
        #Возврат URL-адреса для оплаты
        return session['url']

