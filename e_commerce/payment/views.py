import json
import environ
import razorpay
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from razorpay import Client
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import TemplateView
from .models import Payment
from account.models import ShopUser
from order.models import Order
from .serializers import (
    PaymentSerializer,
    StartPaymentSerializer,
    PaymentSuccessSerializer,
)

# env = environ.Env()

# you have to create .env file in same folder where you are using environ.Env()
# reading .env file which located in api folder
# pre-commit tool has been added to this project
# RAZOR_KEY_ID = 'rzp_test_1THXoALqJ9SdD9' RAZOR_KEY_SECRET = 'D0NcdUzWOcrld06gXNKLQ6sr'

# environ.Env.read_env()


class StartPayment(APIView):
    def post(self, request):
        serializer = StartPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data["amount"]
        name = serializer.validated_data["name"]

        client = razorpay.Client(
            auth=("rzp_test_1THXoALqJ9SdD9", "D0NcdUzWOcrld06gXNKLQ6sr")
        )

        payment_detail = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )

        pay = Payment.objects.create(
            payment_product=name, payment_amount=amount, payment_id=payment_detail["id"]
        )

        serializer = PaymentSerializer(pay)

        data = {"payment": payment_detail, "order": serializer.data}

        return Response(data)


# @api_view(["POST"])
# def start_payment(request):
#     # request.data is coming from frontend

#     amount = request.data["amount"]
#     name = request.data["name"]

#     # setup razorpay client this is the client to whome user is paying money that's you
#     client = razorpay.Client(
#         auth=("rzp_test_1THXoALqJ9SdD9", "D0NcdUzWOcrld06gXNKLQ6sr")
#     )

#     # create razorpay order
#     # the amount will come in 'paise' so multiply with 100
#     payment_detail = client.order.create(
#         {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
#     )

#     # we are saving an order with isPaid=False because we've just initialized the order
#     # we haven't received the money we will handle the payment succes in next
#     # function
#     pay = Payment.objects.create(
#         payment_product=name, payment_amount=amount, payment_id=payment_detail["id"]
#     )

#     serializer = PaymentSerializer(pay)

#     """order response will be
#     {'id': 17,
#     'order_date': '23 January 2021 03:28 PM',
#     'order_product': '**product name from frontend**',
#     'order_amount': '**product amount from frontend**',
#     'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
#     'isPaid': False}"""

#     data = {"payment": payment_detail, "order": serializer.data}
#     return Response(data)


class PaymentView(TemplateView):
    template_name = "pay.html"


class PaymentSuccess(APIView):
    def post(self, request):
        serializer = PaymentSuccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        razorpay_payment_id = serializer.validated_data["razorpay_payment_id"]
        razorpay_order_id = serializer.validated_data["razorpay_order_id"]
        razorpay_signature = serializer.validated_data["razorpay_signature"]

        client = Client(auth=("rzp_test_1THXoALqJ9SdD9", "D0NcdUzWOcrld06gXNKLQ6sr"))

        data = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature,
        }

        try:
            client.utility.verify_payment_signature(data)
            payment = Payment.objects.get(payment_id=razorpay_order_id)
            payment.is_paid = True
            payment.save()
            order = Order.objects.get(cart_id=1)
            order.status = "C"
            order.save()
        except:
            res_data = {"message": "Payment authentication failed!!!"}
            return Response(res_data)
        res_data = {"message": "payment successfully received!"}
        return Response(res_data)


# @csrf_exempt
# @api_view(["POST"])
# def payment_success(request):
#     if request.method == "POST":
#         # Get the payment details from the request
#         razorpay_payment_id = request.data.get("razorpay_payment_id")
#         razorpay_order_id = request.data.get("razorpay_order_id")
#         razorpay_signature = request.data.get("razorpay_signature")

#         # Verify the payment signature
#         client = Client(auth=("rzp_test_1THXoALqJ9SdD9", "D0NcdUzWOcrld06gXNKLQ6sr"))
#         data = {
#             "razorpay_order_id": razorpay_order_id,
#             "razorpay_payment_id": razorpay_payment_id,
#             "razorpay_signature": razorpay_signature,
#         }
#         try:
#             client.utility.verify_payment_signature(data)
#             # cart = request.user.get_cart()
#             payment = Payment.objects.get(payment_id=razorpay_order_id)
#             payment.is_paid = True
#             payment.save()
#             order = Order.objects.get(cart_id=1)
#             order.status = "C"
#             order.save()

#         except:
#             # Handle the signature verification error
#             res_data = {"message": "Payment authentication failed!!!"}
#             return Response(res_data)

#         # Payment signature is valid. Handle the payment success
#         print("order_id:", razorpay_order_id)
#         print("Payment_id:", razorpay_payment_id)
#         print("Payment_signature:", razorpay_signature)
#         print("Payment Successful")
#         res_data = {"message": "payment successfully received!"}
#         return Response(res_data)

#     # Return a bad request response if the request method is not POST
#     return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
