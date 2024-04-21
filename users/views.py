from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

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

        if 'uid' in response.json():
            return HttpResponseRedirect('/resend-activation')
        elif 'token' in response.json():
            return HttpResponseRedirect('/resend-activation')
        elif 'detail' in response.json():
            return HttpResponseRedirect('/login')#, message="Account has been activated"

