from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        # depth = 2


class StartPaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    name = serializers.CharField()


class PaymentSuccessSerializer(serializers.Serializer):
    razorpay_payment_id = serializers.CharField()
    razorpay_order_id = serializers.CharField()
    razorpay_signature = serializers.CharField()
