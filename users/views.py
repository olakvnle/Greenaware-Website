from django.core.mail import EmailMessage, get_connection
from django.http import JsonResponse
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


class ObserverRegisterationView(View):
    def get(self, request):
        ty = request.GET.get('ty', None)
        context = {'type':ty}
        return render(request, 'new/observer.html',context)

    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            password = data['password']
            re_password = data['re_password']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'email_error': 'Email already registered'}, status=400)

            if len(password) < 8:
                return JsonResponse({'password_error': 'Password must be at least 8 characters'}, status=400)

            if password != re_password:
                return JsonResponse({'re_password_error': 'Passwords do not match'}, status=400)

            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.is_active = False
            user.is_observer = True
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            activate_url = 'http://' + domain + link

            email_subject = 'Activate your account'
            email_body = f'Hi {user.first_name},\nPlease use this link to activate your account: {activate_url}'
            email = EmailMessage(email_subject, email_body, 'admin@rashkemsoft.com.ng', [email])
            email.send(fail_silently=False)

            return JsonResponse({'success': 'Account created successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class SubscriberRegisterationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')


class LoginView(View):
    def get(self, request):
        return render(request, 'new/login.html')

    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        if email and password:
            user = auth.authenticate(email=email, password=password)
            if user.is_active:
                auth.login(request, user)
                url = '/observer/dashboard' if user.is_observer else '/subscriber/dashboard'
                return JsonResponse({'msg': url})

            return JsonResponse({'activate_error': 'Account is not Activated'}, status=400)

        return JsonResponse({'error': 'This credential is not valid'}, status=400)


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully')
        return redirect('login')


class ActivateObserverView(View):
    def get(self, request, uidb64, token):
        try:

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            token = account_activation_token.check_token(user, token)

            if not token:
                messages.info(request, 'Account has already been Activation successful.')
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

    # def get(self, request, uid, token):
    #     activation_url = f'http://127.0.0.1:8090/api/users/activation/'
    #
    #     response = requests.post(
    #         activation_url,
    #         json={'uid': uid, 'token': token},
    #         timeout=5,
    #         verify=False,  # Disable SSL verification (only for development/testing)
    #         headers={'Content-Type': 'application/json'}
    #     )
    #     if response.status_code == 204:
    #         messages.success(request, 'Activation successful.')
    #         return HttpResponseRedirect('/observer/login')
    #
    #     if 'detail' in response.json():
    #         messages.info(request, 'Account has already been Activation successful.')
    #         return HttpResponseRedirect('/observer/login')
    #     elif 'token' in response.json():
    #         return HttpResponseRedirect('/resend-activation')
    #     elif 'uid' in response.json():
    #         return HttpResponseRedirect('/resend-activation')

# def register(request, register_url):
#     # Get User data
#     email = request.POST['email']
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     password = request.POST['password']
#     re_password = request.POST['re_password']
#
#     context = {'fieldValues': request.POST}
#
#     # Validate and Save User
#     if not User.objects.filter(email=email).exists():
#         if len(password) < 8:
#             messages.error(request, 'Password must be at least 8 characters')
#             return render(request, 'auth/register.html', context)
#         if not User.objects.filter(email=email).exists():
#             if len(password) < 6:
#                 messages.error(request, 'Password is too short')
#                 return render(request, 'auth/register.html', context)
#             user = User.objects.create_user(username=username, email=email)
#             user.set_password(password)
#             user.is_active = False
#             user.save()
#
#             uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
#             domain = get_current_site(request).domain
#             link = reverse('activate', kwargs={
#                 'uidb64': uidb64,
#                 'token': account_activation_token.make_token(user)
#             })
#
#             activate_url = 'http://' + domain + link
#
#             email_subject = 'Activate your account'
#             email_body = 'Hi Welcome ' + user.username + \
#                          'Please use this link to activate your account\n ' + activate_url
#             email = EmailMessage(
#                 email_subject,
#                 email_body,
#                 'admin@rashkemsoft.com.ng',
#                 [email],
#             )
#
#             try:
#                 # Send the email
#                 email.send(fail_silently=False)
#                 messages.success(request, 'Account created successfully')
#
#             except Exception as e:
#
#                 # Handle any exceptions, log the error, or perform appropriate actions
#                 messages.error(request, e)
#             # finally:
#             #     # Close the connection after sending the email, whether successful or not
#             #     connection.close()
#
#             return render(request, 'auth/register.html')
#
#     return render(request, 'auth/register.html')
