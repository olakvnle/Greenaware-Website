from django.core.mail import EmailMessage, get_connection
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from users.models import UserAccount as User
import json
# from validate_email import validate_email
from django.contrib import messages
from django.utils.encoding import force_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .util import account_activation_token
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


class ObserverRegisterationView(View):
    def get(self, request):

        return render(request, 'new/observer.html')

    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            password = data['password']
            re_password = data['re_password']
            register_type = data['type']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'email_error': 'Email already registered'}, status=400)

            if len(password) < 8:
                return JsonResponse({'password_error': 'Password must be at least 8 characters'}, status=400)

            if password != re_password:
                return JsonResponse({'re_password_error': 'Passwords do not match'}, status=400)

            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            if register_type == 'observer':
                user.is_observer = True
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activation',
                           kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            activate_url = 'http://' + domain + link

            email_subject = 'Activate your account'
            email_body = f'Hi {user.first_name},\nPlease use this link to activate your account: {activate_url}'
            email = EmailMessage(email_subject, email_body, 'admin@rashkemsoft.com.ng', [email])
            email.send(fail_silently=False)

            return JsonResponse({'success': 'Account created successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class LoginView(View):
    def get(self, request):
        return render(request, 'new/login.html')

    def post(self, request):

        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        if email and password:
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    url = '/observer/dashboard' if user.is_observer else '/subscriber/dashboard'
                    return JsonResponse({'msg': url})
                else:
                    return JsonResponse({'activate_error': 'Account is not Activated'}, status=400)
            else:
                return JsonResponse({'error': 'This credential is not valid'}, status=400)


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully')
        return redirect('login')


class ActivateUserView(View):
    def get(self, request, uidb64, token):

        try:

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            token = account_activation_token.check_token(user, token)

            if not token:
                messages.info(request, 'Account Activation Successful.')
                return HttpResponseRedirect('/login')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')
        except Exception as ex:
            pass

        return redirect('login')


class ActivateObserverView(View):
    def get(self, request, uid, token):
        context = {'uid': uid, 'token': token}
        return render(request, 'new/activate.html', context)


@csrf_exempt
def store_tokens(request):
    if request.method == 'POST':
        try:
            # Extract tokens from request body
            data = json.loads(request.body)
            access_token = data.get('access')
            refresh_token = data.get('refresh')
            # Store tokens in session and cookie
            request.session['jwt_access_token'] = access_token
            request.session['jwt_refresh_token'] = refresh_token
            response = JsonResponse({'message': 'Tokens stored successfully'})
            response.set_cookie('jwt_access_token', access_token, httponly=True, secure=True)
            response.set_cookie('jwt_refresh_token', refresh_token, httponly=True, secure=True)
            return response  # Return the response object

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

