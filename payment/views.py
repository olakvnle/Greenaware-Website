from django.shortcuts import render
import stripe
from django.shortcuts import redirect
import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'subscriber/payment.html', {'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY})

    def post(self, request):
        try:
            price =49
            # Token is created using Stripe.js or Checkout!
            # Get the payment token ID submitted by the form:
            token = request.POST['stripeToken']

            # Create a charge: this will charge the user's card
            charge = stripe.Charge.create(
                amount=price * 100,
                currency='usd',
                description='Example charge',
                source=token,
            )

            # Handle successful payment (e.g., update database, send confirmation email)
            return render(request, 'subscriber/payment_success.html')
        except stripe.error.CardError as e:
            # Since it's a decline, stripe.error.CardError will be caught
            body = e.json_body
            err = body.get('error', {})
            print("Status is: %s" % e.http_status)
            print("Type is: %s" % err.get('type'))
            print("Code is: %s" % err.get('code'))
            # param is '' in this case
            print("Param is: %s" % err.get('param'))
            print("Message is: %s" % err.get('message'))
            return render(request, 'subscriber/payment.html', {'error_message': err.get('message')})
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            return render(request, 'subscriber/payment.html',
                          {'error_message': 'Rate limit error. Please try again later.'})
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            return render(request, 'payment_form.html',
                          {'error_message': 'Invalid request error. Please check your input.'})
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            return render(request, 'subscriber/payment.html',
                          {'error_message': 'Authentication error. Please check your API keys.'})
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            return render(request, 'subscriber/payment.html',
                          {'error_message': 'Network error. Please check your internet connection.'})
        except stripe.error.StripeError as e:
            # Display a very generic error to the user
            return render(request, 'subscriber/payment.html',
                          {'error_message': 'An error occurred. Please try again later.'})
        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            return render(request, 'subscriber/payment.html', {'error_message': str(e)},
                          {'error_message': 'An unexpected error occurred. Please try again later.'})
        else:
            return redirect('payment')


class PaymentSuccessView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'subscriber/payment_success.html')
