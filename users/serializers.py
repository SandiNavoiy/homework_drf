from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = "__all__"

    def get_payments(self, instance):
        """Добавление истории платежей """
        payments_list = []
        if instance.payments_set.all():
            for i in instance.payments_set.all().values_list():
                pay_list = []
                #дата
                pay_list.append(i[1].strftime("%d/%m/%Y"))
                #сумма платежа
                pay_list.append(i[4])
                #тип оплаты
                payments_list.append(pay_list)

            return payments_list
        return None
