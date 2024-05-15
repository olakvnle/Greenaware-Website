import json
from django.shortcuts import redirect
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .auth import IsNotObserverMixin,IsNotSubscriberMixin


# class EmailValidationView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         email = data['email']
#         if not validate_email(email):
#             return JsonResponse({'email_error': 'Invalid Email'}, status=400)
#         if User.objects.filter(email=email).exists():
#             return JsonResponse({'email_error': 'Email already exists'}, status=400)
#         return JsonResponse({'email_valid': True})


class IndexView(View):
    def get(self, request):
        context = {}
        return render(request, 'new/index.html')


class APIView(View):
    def get(self, request):
        context = {
            'type': 'subscriber'
        }
        return render(request, 'new/api.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'new/about.html')


class PricingView(View):
    def get(self, request):
        return render(request, 'new/pricing.html')


class PricingPlanView(View):
    def get(self, request):
        return render(request, 'new/pricing_plan.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'new/contact.html')


class ObserverView(View):
    def get(self, request):
        return render(request, 'new/observer_welcome_note.html')


class DashboardView(LoginRequiredMixin,IsNotObserverMixin,View):
    def get(self, request):

        context = {
            'page_name': 'Dashboard'
        }
        return render(request, 'observer/dashboard.html', context)


class ObservationRecordView(LoginRequiredMixin,IsNotObserverMixin,View):

    def get(self, request):

        context = {
            'page_name': 'Observation'
        }
        return render(request, 'observer/view_observation.html', context)


class CourseView(LoginRequiredMixin,IsNotObserverMixin,View):
    def get(self, request):

        context = {
            'page_name': 'Courses'
        }

        return render(request, 'observer/course.html', context)


class ObservationView(LoginRequiredMixin,IsNotObserverMixin,View):
    def get(self, request):

        context = {
            'page_name': 'Observation'
        }
        user = request.user
        if user.take_online_course:
            return render(request, 'observer/observation.html', context)
        else:
            messages.success(request, 'Please take the course first.')
            return render(request, 'observer/course.html')


class ObserverUserView(LoginRequiredMixin,IsNotObserverMixin,View):
    def get(self, request):
        return render(request, 'observer/user.html')


class UserView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'subscriber/user.html')


class SubscriberDashboardView(LoginRequiredMixin,IsNotSubscriberMixin, View):
    def get(self, request):
        return render(request, 'subscriber/dashboard.html')


class SubscriberAPIView(LoginRequiredMixin,IsNotSubscriberMixin, View):
    def get(self, request):
        return render(request, 'subscriber/api_access.html')


class SubscriberPriceAPIView(LoginRequiredMixin,IsNotSubscriberMixin, View):
    def get(self, request):
        context = {
            'page_name': 'Pricing'
        }
        return render(request, 'subscriber/pricing.html', context)


class CourseSubmitView(View):
    def post(self, request):

        try:
            if request.user.is_authenticated:
                user = request.user
                user.take_online_course = True
                user.save()
                return JsonResponse({'success': True}, status=200)
            else:
                return JsonResponse({'success': False, 'error': 'User is not authenticated'}, status=401)
        except KeyError:
            return JsonResponse({'success': False, 'error': 'Invalid request data'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
