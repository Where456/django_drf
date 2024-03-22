import os

import stripe
from dotenv import load_dotenv

from users.models import Payment

load_dotenv()


def get_pay(amount_payment, user):
    stripe.api_key = os.getenv("TOKEN")
    pay = stripe.PaymentIntent.create(
        amount=amount_payment,
        currency="usd",
        automatic_payment_methods={"enabled": True}
    )

    payment = Payment.objects.create(
        user=user,
        amount_payment=amount_payment,
        stripe_id=pay.id
    )

    return payment
