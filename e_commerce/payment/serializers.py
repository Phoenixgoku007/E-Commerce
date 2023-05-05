from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    PaymentSerializer to serialize all the fiedls present in the Payment model.
    """

    class Meta:
        model = Payment
        fields = "__all__"
        # depth = 2


class StartPaymentSerializer(serializers.Serializer):
    """
    StartPaymentSerializer to serialize only the amount and name field which are used in StartPayment View for initiating the payment process
    """

    amount = serializers.IntegerField()
    name = serializers.CharField()


class PaymentSuccessSerializer(serializers.Serializer):
    """
    PaymentSuccessSerializer to serialize only these three fields
    which are used in PaymentSuccess view for verifying and completing the payment process
    """

    razorpay_payment_id = serializers.CharField()
    razorpay_order_id = serializers.CharField()
    razorpay_signature = serializers.CharField()
