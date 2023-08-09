from rest_framework import serializers

from Subscription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериалайзер"""

    class Meta:
        model = Subscription
        fields = "__all__"
