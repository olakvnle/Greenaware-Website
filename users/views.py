from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
import requests


class ActivateObserverView(View):
    def get(self, request, uid, token):
        activation_url = f'http://127.0.0.1:8000/api/v1/users/activation/'

        response = requests.post(
            activation_url,
            json={'uid': uid, 'token': token},
            timeout=5,
            verify=False,  # Disable SSL verification (only for development/testing)
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 204:
            messages.success(request, 'Activation successful.')
            return HttpResponseRedirect('/observer/login')

        if 'detail' in response.json():
            messages.info(request,'Account has already been Activation successful.')
            return HttpResponseRedirect('/observer/login')
        elif 'token' in response.json():
            return HttpResponseRedirect('/resend-activation')
        elif 'uid' in response.json():
            return HttpResponseRedirect('/resend-activation')
