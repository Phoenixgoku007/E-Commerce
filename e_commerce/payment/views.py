import json
import environ
import razorpay
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer

env = environ.Env()

# you have to create .env file in same folder where you are using environ.Env()
# reading .env file which located in api folder
# pre-commit tool has been added to this project
# RAZOR_KEY_ID = 'rzp_test_1THXoALqJ9SdD9' RAZOR_KEY_SECRET = 'D0NcdUzWOcrld06gXNKLQ6sr'
environ.Env.read_env()


@api_view(["POST"])
def start_payment(request):
    # request.data is coming from frontend

    amount = request.data["amount"]
    name = request.data["name"]

    # setup razorpay client this is the client to whome user is paying money that's you
    client = razorpay.Client(
        auth=("rzp_test_1THXoALqJ9SdD9", "D0NcdUzWOcrld06gXNKLQ6sr")
    )

    # create razorpay order
    # the amount will come in 'paise' that means if we pass 50 amount will become
    # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will
    # mumtiply it by 100 so it will be 50 rupees.
    payment_detail = client.order.create(
        {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
    )

    # we are saving an order with isPaid=False because we've just initialized the order
    # we haven't received the money we will handle the payment succes in next
    # function
    pay = Payment.objects.create(
        payment_product=name, payment_amount=amount, payment_id=payment_detail["id"]
    )

    serializer = PaymentSerializer(pay)

    """order response will be 
    {'id': 17, 
    'order_date': '23 January 2021 03:28 PM', 
    'order_product': '**product name from frontend**', 
    'order_amount': '**product amount from frontend**', 
    'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""

    data = {"payment": payment_detail, "order": serializer.data}
    return Response(data)


@api_view(["POST"])
def verify_payment(request):
    # get the payment_id and razorpay_payment_id from the POST request
    payment_id = request.data.get("payment_id")
    razorpay_payment_id = request.data.get("razorpay_payment_id")

    # create a razorpay client
    client = razorpay.Client(
        auth=("rzp_test_1THXoALqJ9SdD9", "D0NcdUzWOcrld06gXNKLQ6sr")
    )

    # fetch the payment details from Razorpay
    payment = client.payment.fetch(razorpay_payment_id)

    # check if the payment amount and currency match the order
    if payment["amount"] != order.payment_amount * 100 or payment["currency"] != "INR":
        return Response({"message": "Payment verification failed."}, status=400)

    # update the order status if the payment is successful
    if payment["status"] == "captured":
        order = Payment.objects.get(payment_id=payment_id)
        order.is_paid = True
        order.save()
        return Response(
            {"message": "Payment verified and order status updated."}, status=200
        )

    return Response({"message": "Payment verification failed."}, status=400)
