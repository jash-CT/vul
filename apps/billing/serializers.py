from rest_framework import serializers
from .models import Payment, Subscription

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'payment_date', 'payment_method']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'start_date', 'end_date', 'is_active']