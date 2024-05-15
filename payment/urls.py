from django.urls import path
from payment.views import PaymentView,PaymentSuccessView

urlpatterns = [

    path('subscriber/payment/', PaymentView.as_view(), name='payment'),
    path('subscriber/payment/success/', PaymentSuccessView.as_view(), name='payment-success'),

]
